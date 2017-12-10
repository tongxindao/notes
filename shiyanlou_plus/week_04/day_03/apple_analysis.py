#_*_ coding:utf-8 _*_

import pandas as pd


def quarter_volume(index):
    try: 
        index = int(index)
    except:
        print("Please input number.")
        exit(-1)

    if index <= 0:
        index = 1

    data = pd.read_csv("apple.csv", header=0)
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.set_index("Date")

    sort_data_by_quarter = data.resample("Q").sum().sort_values(
            by="Volume", ascending=False)

    second_volume = int(str(sort_data_by_quarter[index-1:index]).split()[-1])

    return second_volume


if __name__ == "__main__":
    index = input("Please input your want to know quarter sort index: ")
    second_volume = quarter_volume(index)
    print("Second Volume: {0}".format(second_volume))
