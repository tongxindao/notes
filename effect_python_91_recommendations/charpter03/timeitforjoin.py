import timeit

strlist = ["It is a long value string will not keep in memory" for n in range(100000)]


def join_test():
    return " ".join(strlist)


def plus_test():
    result = ""
    for i, v in enumerate(strlist):
        result = result + v
    return result


if __name__ == "__main__":
    jointimer = timeit.Timer("join_test()", "from __main__ import join_test")
    print(jointimer.timeit(number = 100000))
    plustimer = timeit.Timer("plus_test()", "from __main__ import plus_test")
    print(plustimer.timeit(number = 100000))
