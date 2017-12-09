#_*_ coding:utf-8 _*_

import pandas as pd


def quarter_volume():
    date = pd.read_csv("apple.csv", header=0)

    second_volume = date.sort_values(by="Volume", ascending=False)[1:2]

    return second_volume


if __name__ == "__main__":
    second_volume = quarter_volume()
    print("Second Volume: {0}".format(second_volume))
