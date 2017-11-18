import sys
from decimal import Decimal


def get_salary(salary):
    try:
        salary = abs(int(salary))
        if salary > 0:
            return salary
        else:
            raise
    except BaseException:
        print("Parameter Error")
        sys.exit(0)


def cal_social_security(salary):
    pension = 0.08
    medical = 0.02
    unemployment = 0.005
    injury = 0.00
    matermity = 0.00
    provident = 0.06

    social_security_tax = pension + medical \
        + unemployment + injury + matermity + provident
    social_security = salary * social_security_tax

    return social_security


def cal_taxable_income(salary, social_security):
    start_point = 3500
    taxable_income = 0

    taxable_income = salary - social_security - start_point

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


def main():
    try:
        information = {}
        for arg in sys.argv[1:]:
            job_number = arg.split(":")[0]
            before_salary = arg.split(":")[1]
            information[job_number] = before_salary

            salary = get_salary(information[job_number])
            social_security = cal_social_security(salary)
            taxable_income = cal_taxable_income(salary, social_security)
            tax = calculator_tax(taxable_income)
            after_salary = after_salary_tax(salary, social_security, tax)

            information[job_number] = after_salary

            print(
                "{0}:{1}".format(
                    job_number, Decimal(
                        information[job_number]).quantize(
                        Decimal(".01"))))
    except IndexError:
        print("Please input \'job_number:salary\' format parameter!")


if __name__ == "__main__":
    main()
