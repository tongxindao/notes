import sys
from math import *
from ast import literal_eval

def ExpCalcBot(string):
    try:
        print("Your answer is", literal_eval(string))
    except NameError:
        print("The expression you enter is not valid")


print("Hi,I am ExpCalcBot. please input your experssion or enter e to end")
inputstr = ""

while True:
    print("Please enter a number or operation. press Enter to complete. :")
    inputstr = input()

    if inputstr == str("e"):
        sys.exit()
    elif str(inputstr) != str(""):
        ExpCalcBot(inputstr)
        inputstr = ""
