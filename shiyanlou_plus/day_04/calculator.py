#!/usr/bin/env python3

import os
import sys
import csv
import time
import queue
import getopt
import random
import multiprocessing

from decimal import Decimal


def process_config(config_file):
    try:
        with open(config_file, "r") as config:
            social_security_percent = {}
            for line in config:
                item = line.split("=")[0].strip()
                number = line.split("=")[1].strip()
                social_security_percent[item] = number
            return social_security_percent
    except BaseException as e:
        print("process_config func Exception: {0}".format(e))
        sys.exit(0)


def process_data(data_file, queue_for_get_calc_data):
    try:
        with open(data_file, "r") as data:
            for job_number, salary in csv.reader(data, delimiter=","):
                salary_data = []
                salary_data.append(job_number)
                salary_data.append(salary)
                queue_for_get_calc_data.put_nowait(salary_data)
                salary_data = []
    except BaseException as e:
        print("process_data func Exception: {0}".format(e))
        sys.exit(0)


def parsing_parameter(argv):
    try:
        opts, args = getopt.getopt(
            argv, "c:d:o:", [
                "config=", "data=", "output="])
    except getopt.GetoptError as e:
        print("{0}\n\'./calculator.py -c <cfg> -d <src> -o <dst>\'".format(e))
        sys.exit(0)

    try:
        for opt, arg in opts:
            if opt in ("-c", "--config"):
                social_security_percent = process_config(arg)
            elif opt in ("-d", "--data"):
                data_file = arg
            elif opt in ("-o", "--output"):
                output_file = arg
        return social_security_percent, data_file, output_file
    except BaseException as e:
        print("parsing_parameter func Exception: {0}".format(e))
        sys.exit(0)


def get_salary(salary):
    try:
        salary = abs(int(salary))
        if salary > 0:
            return salary
        else:
            raise
    except BaseException as e:
        print("get_salary func Exception: {0}".format(e))
        sys.exit(0)


def cal_social_security(baselow, basehigh, pension, medical,
                        unemployment, injury, matermity, provident, salary):

    social_security_tax = pension + medical \
        + unemployment + injury + matermity + provident

    if salary < baselow:
        social_security = baselow * social_security_tax
    elif salary > basehigh:
        social_security = basehigh * social_security_tax
    else:
        social_security = salary * social_security_tax

    return social_security


def cal_taxable_income(salary, social_security):
    start_point = 3500
    taxable_income = 0

    taxable_income = salary - social_security - start_point

    if taxable_income <= 0:
        taxable_income = 0

    return taxable_income


def calculator_tax(taxable_income):
    if taxable_income == 0:
        tax = 0
    elif taxable_income <= 1500:
        tax = taxable_income * 0.03 - 0
    elif 1500 < taxable_income <= 4500:
        tax = taxable_income * 0.1 - 105
    elif 4500 < taxable_income <= 9000:
        tax = taxable_income * 0.2 - 555
    elif 9000 < taxable_income <= 35000:
        tax = taxable_income * 0.25 - 1005
    elif 35000 < taxable_income <= 55000:
        tax = taxable_income * 0.3 - 2755
    elif 55000 < taxable_income <= 80000:
        tax = taxable_income * 0.35 - 5505
    else:
        tax = taxable_income * 0.45 - 13505
    return tax


def after_salary_tax(salary, social_security, tax):
    after_tax_salary = salary - social_security - tax
    return after_tax_salary


def read_from_queue(social_security_percent,
                    queue_for_get_calc_data, queue_for_calc_write_data):

    baselow = float(social_security_percent["JiShuL"])
    basehigh = float(social_security_percent["JiShuH"])
    pension = float(social_security_percent["YangLao"])
    medical = float(social_security_percent["YiLiao"])
    unemployment = float(social_security_percent["ShiYe"])
    injury = float(social_security_percent["GongShang"])
    matermity = float(social_security_percent["ShengYu"])
    provident = float(social_security_percent["GongJiJin"])

    try:
        while True:
            before_salary_data = queue_for_get_calc_data.get()
            print("queue_for_get_calc_data.get: {0}".format(before_salary_data))
            job_number = before_salary_data[0]
            before_salary = before_salary_data[1]

            salary = get_salary(before_salary)
            social_security = cal_social_security(baselow, basehigh, pension,
                                                  medical, unemployment,
                                                  injury, matermity, provident,
                                                  salary)
            taxable_income = cal_taxable_income(salary, social_security)
            tax = calculator_tax(taxable_income)
            after_salary = after_salary_tax(salary, social_security, tax)

            social_security = str(
                Decimal(social_security).quantize(
                    Decimal(".01")))
            tax = str(Decimal(tax).quantize(Decimal(".01")))
            after_salary = str(Decimal(after_salary).quantize(Decimal(".01")))

            output_info = [
                job_number,
                salary,
                social_security,
                tax,
                after_salary]
            queue_for_calc_write_data.put_nowait(output_info)
            output_info = []
    except queue.Empty:
        queue_for_get_calc_data.close()


def write_to_csv(output_file, queue_for_calc_write_data):
    try:
        with open(output_file, "a") as output:
            output_data = csv.writer(output, delimiter=",")
            while True:
                information = queue_for_calc_write_data.get()
                output_data.writerow(information)
    except (BaseException, queue.Empty) as e:
        print("write_to_csv func Exception: {0}".format(e))
        queue_for_calc_write_data.close()
        sys.exit(0)


def main():
    social_security_percent, data_file, output_file = parsing_parameter(
        sys.argv[1:])

    queue_for_get_calc_data = multiprocessing.Queue()
    queue_for_calc_write_data = multiprocessing.Queue()

    read_procs = multiprocessing.Process(
        target=process_data, args=(
            data_file, queue_for_get_calc_data))

    calc_procs = multiprocessing.Process(target=read_from_queue,
                                         args=(social_security_percent,
                                               queue_for_get_calc_data,
                                               queue_for_calc_write_data))

    write_procs = multiprocessing.Process(
        target=write_to_csv, args=(
            output_file, queue_for_calc_write_data))

    read_procs.start()
    calc_procs.start()
    write_procs.start()

    read_procs.join()
    calc_procs.join()
    write_procs.join()


if __name__ == "__main__":
    main()
