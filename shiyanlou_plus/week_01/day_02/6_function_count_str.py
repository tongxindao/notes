#!/usr/bin/env python3
from collections import Counter


def char_count(str):
    # char_list = set(str)
    # for char in char_list:
    #     print(char, str.count(char))
    c = Counter(str)
    counters = c.most_common(len(str))
    for i in range(len(counters)):
        print(counters[i])


if __name__ == "__main__":
    s = input("Enter a string: ")
    char_count(s)
