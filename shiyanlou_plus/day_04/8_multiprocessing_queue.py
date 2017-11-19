from multiprocessing import Process, Queue

queue = Queue()


def f1(queue):
    queue.put("Hello shiyanlou")


def f2(queue):
    while queue.empty():
        data = queue.get()
        print(data)


def main():
    queue = Queue()
    p1 = Process(target=f1, args=(queue, ))
    p2 = Process(target=f2, args=(queue, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
