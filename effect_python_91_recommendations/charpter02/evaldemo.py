import sys
from math import *


def ExpCalcBot(string):
    try:
        math_fun_list = ["acos", "asin", "atan", "cos", "e", "log", "log10", "pi", "pow", "sin", "sqrt", "tan"]
        math_fun_dict = dict([(k, globals().get(k)) for k in math_fun_list])
        print("Your answer is", eval(string, {"__builtins__": None}, math_fun_dict))
    except NameError:
        print("The expression you enter is not valid")


print("Hi,I am ExpCalcBot. please input your experssion or enter e to end")
inputstr = ""

while True:
    print("Please enter a number or operation. press Enter to complete. :")
    inputstr = input()

    if inputstr == str("e"):
        sys.exit()
    elif repr(inputstr) != repr(""):
        ExpCalcBot(inputstr)
        inputstr = ""
