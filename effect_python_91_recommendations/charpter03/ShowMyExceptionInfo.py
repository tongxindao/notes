import sys
import traceback

ItemPriceTable = {"apple":"3.5", "orange":"4", "cheery":"20", "mango":"8"}


def GetPrice(itemname):

    try:
        price = ItemPriceTable[itemname]
        return price
    except KeyError:
        print("%s can not find in the price table, you should input another kind of fruit." 
            % sys.exc_info()[1])


while True:
    itemname = input("Enter the fruit name to get the price or press x to exit: ")
    if itemname == "x":
        break
    price = GetPrice(itemname)
    if price != None:
        print("%s's price is $%s/kg" % (itemname, price))
