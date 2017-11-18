import sys
from decimal import Decimal


def cal_taxable_income(salary):
    try:
        social_security = 0
        start_point = 3500
        salary = int(salary)
        taxable = 0
        taxable_income = 0

        if salary > 0:
            taxable = salary - social_security - start_point
        if taxable >= 0:
            taxable_income = taxable
        return taxable_income
    except:
        print("Parameter Error")


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
    print("{0}".format(Decimal(tax).quantize(Decimal('.01'))))
    return tax


def main():
    try:
        salary = sys.argv[1]
        taxable_income = cal_taxable_income(salary)
        calculator_tax(taxable_income)
    except IndexError:
        print("must be input a integer number parameter!")


if __name__ == "__main__":
    main()
