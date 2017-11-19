#!/usr/bin/env python3

import os
import sys
import csv
import time
import random
import getopt

from decimal import Decimal
from multiprocessing import Process, Queue


def process_config(config_file):
    social_security_percent = {}

    try:
        if(os.path.exists(config_file)):
            with open(config_file, "r") as config:
                for line in config:
                    item = line.split("=")[0].strip()
                    number = line.split("=")[1].strip()
                    social_security_percent[item] = number
                return social_security_percent
    except FileNotFoundError as e:
        print("config file not found: {0}".format(e))
        sys.exit(0)


def process_data(data_file, queue_for_get_calc_data):
    salary_data = {}

    try:
        if(os.path.exists(data_file)):
            with open(data_file, "r") as data:
                for job_number, salary in csv.reader(data, delimiter=","):
                    salary_data[job_number] = salary
                    queue_for_get_calc_data.put(salary_data)
                    print("put salary data is: {0}".format(salary_data))
                    print("put salary process id is: {0}".format(os.getpid()))
    except BaseException as e:
        print("data file not found: {0}".format(e))
        sys.exit(0)


def parsing_parameter(argv):
    social_security_percent = {}
    # salary_data = {}
    data_file = ""
    output_file = ""

    try:
        opts, args = getopt.getopt(
            argv, "c:d:o:", [
                "config=", "data=", "output="])
    except getopt.GetoptError as e:
        print(
            "{0}\n\'./calculator.py -c <cfg> -d <src> -o <dst>\'".format(e))
        sys.exit(0)

    try:
        for opt, arg in opts:
            if opt in ("-c", "--config"):
                social_security_percent = process_config(arg)
            elif opt in ("-d", "--data"):
                data_file = arg
                # salary_data = process_data(arg, queue)
            elif opt in ("-o", "--output"):
                output_file = arg
        return social_security_percent, data_file, output_file
        # return social_security_percent, salary_data, output_file
    except BaseException as e:
        print("Please confirm your parameter: {0}".format(e))
        sys.exit(0)


def get_salary(salary):
    try:
        salary = abs(int(salary))
        if salary > 0:
            return salary
        else:
            raise
    except BaseException as e:
        print("Salary must be lagger than zero: {0}".format(e))
        sys.exit(0)


def cal_social_security(
        baselow,
        basehigh,
        pension,
        medical,
        unemployment,
        injury,
        matermity,
        provident,
        salary):

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


def write_to_csv(output_file, queue_for_calc_write_data):
    try:
        if(os.path.exists(output_file)):
            with open(output_file, "a") as output:
                output_data = csv.writer(output, delimiter=",")
                if not queue_for_calc_write_data.empty():
                    while True:
                        information = queue_for_calc_write_data.get(True)
                        print(
                            "Write data to csv process id: {0}".format(
                                os.getpid()))
                        print("write to csv value is: {0}".format(information.values()))
                        output_data.writerows(information.values())
                print("I am write_to_csv func, i do not work")
        else:
            with open(output_file, "w") as output:
                output_data = csv.writer(output, delimiter=",")
                if not queue_for_calc_write_data.empty():
                    while True:
                        information = queue_for_calc_write_data.get(True)
                        print(
                            "Write data to csv process id: {0}".format(
                                os.getpid()))
                        print("write to csv value is: {0}".format(information.values()))
                        output_data.writerows(information.values())
                print("I am write_to_csv func, i do not work")
    except BaseException as e:
        print("Exception: {0}".format(e))
        sys.exit(0)


def read_from_dict(
        social_security_percent,
        queue_for_get_calc_data,
        queue_for_calc_write_data):
    try:
        information = {}
        output_info = []
        job_number = ""

        baselow = float(social_security_percent["JiShuL"])
        basehigh = float(social_security_percent["JiShuH"])
        pension = float(social_security_percent["YangLao"])
        medical = float(social_security_percent["YiLiao"])
        unemployment = float(social_security_percent["ShiYe"])
        injury = float(social_security_percent["GongShang"])
        matermity = float(social_security_percent["ShengYu"])
        provident = float(social_security_percent["GongJiJin"])

        print(queue_for_get_calc_data.empty())
        if not queue_for_get_calc_data.empty():
            while True:
                salary_data = queue_for_get_calc_data.get(True)
                print("get from process_data value is: {0}".format(salary_data))
                job_number = salary_data.keys()
                before_salary = salary_data.values()

                salary = get_salary(before_salary)

                social_security = cal_social_security(
                    baselow,
                    basehigh,
                    pension,
                    medical,
                    unemployment,
                    injury,
                    matermity,
                    provident,
                    salary)

                taxable_income = cal_taxable_income(salary, social_security)
                tax = calculator_tax(taxable_income)

                after_salary = after_salary_tax(salary, social_security, tax)

                social_security = str(
                    Decimal(social_security).quantize(
                        Decimal(".01")))
                tax = str(Decimal(tax).quantize(Decimal(".01")))
                after_salary = str(
                    Decimal(after_salary).quantize(
                        Decimal(".01")))

                output_info = [
                    job_number,
                    salary,
                    social_security,
                    tax,
                    after_salary]
                information[job_number] = output_info

                queue_for_calc_write_data.put(information)
                # time.sleep(random.random())
                print("put to write_to_csv value is: {0}".format(information))
                print("Calc salary process id is: {0}".format(os.getpid()))
        else:
            print("I am calc func, I do not catch anything!!!")
    except BaseException as e:
        print(
            "Please confirm your file path and file content: {0}".format(e))
        sys.exit(0)


def main():
    social_security_percent, data_file, output_file = parsing_parameter(
        sys.argv[1:])

    queue_for_get_calc_data = Queue()
    queue_for_calc_write_data = Queue()

    read_procs = Process(
        target=process_data,
        args=(data_file, queue_for_get_calc_data))

    calc_procs = Process(
        target=read_from_dict,
        args=(social_security_percent,
              queue_for_get_calc_data,
              queue_for_calc_write_data))

    write_procs = Process(
        target=write_to_csv,
        args=(output_file, queue_for_calc_write_data))

    read_procs.start()
    calc_procs.start()
    write_procs.start()

    read_procs.join()
    calc_procs.join()
    write_procs.join()


if __name__ == "__main__":
    main()
