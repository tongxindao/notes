#_*_ coding:utf-8 _*_

import pandas as pd


def quarter_volume():
    data = pd.read_csv("apple.csv", header=0)

    date = str(data.sort_values(by="Volume", ascending=False)[1:2]["Date"]).split()[1]

    year = int(date.split('-')[0])
    month = int(date.split('-')[1])

    if 1<= month <= 3:

    elif 4<= month <= 6:

    elif 7<= month <= 9:

    elif 10<= month <= 12:

    return second_volume


if __name__ == "__main__":
    second_volume = quarter_volume()
    print("Second Volume: {0}".format(second_volume))
