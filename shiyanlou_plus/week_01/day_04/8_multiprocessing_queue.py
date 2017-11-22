from multiprocessing import Process, Queue, current_process


def f1(queue):
    try:
        # if not queue.full():
        shiyanlou = ["Hello", "shiyanlou"]
        queue.put(shiyanlou)
        print("f1 pid {0}, f1 qsize {1}, f1 data is: {2}".format(
            current_process().name, queue.qsize(), shiyanlou))
    except:
        print("full")
        queue.close()


def f2(queue):
    try:
        # if not queue.empty():
        for i in range(queue.qsize()):
            print("f2 pid {0}, qsize is {1}".format(current_process().name, queue.qsize()))
            print("f2 data is: {0}".format(queue.get()))
            i += 1
    except:
        print("empty")
        queue.close()


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
