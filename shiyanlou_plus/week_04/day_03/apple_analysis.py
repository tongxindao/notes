#_*_ coding:utf-8 _*_
import time
import pandas as pd


def quarter_volume(index):
    try: 
        index = int(index)
    except:
        print("Please input number.")
        exit(-1)

    if index <= 0:
        index = 1

    re_read_data = pd.read_csv("apple.csv", header=0, chunksize=5)
    data_list = []
    
    for chunk in re_read_data:
        data_list.append(chunk)

    data = pd.concat(data_list)

    data.Date = pd.to_datetime(data.Date)
    data.index = data.Date

    sort_data_by_quarter = data.resample("Q").sum().sort_values(
            by="Volume", ascending=False)

    second_volume = int(str(sort_data_by_quarter[index-1:index]).split()[-1])
    print(time.time())
    return second_volume


if __name__ == "__main__":
    index = input("Please input your want to know quarter sort index: ")
    second_volume = quarter_volume(index)
    print("Second Volume: {0}".format(second_volume))
