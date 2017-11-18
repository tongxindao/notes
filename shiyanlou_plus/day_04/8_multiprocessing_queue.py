from multiprocessing import Process, Queue

queue = Queue()


def f1():
    queue.put("Hello shiyanlou")


def f2():
    data = queue.get()
    print(data)


def main():
    Process(target=f1).start()
    Process(target=f2).start()


if __name__ == "__main__":
    main()
