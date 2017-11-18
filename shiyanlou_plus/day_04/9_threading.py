import threading


def hello(name):
    # get_ident() 获取当前线程 id
    print("child thread: {}".format(threading.get_ident()))
    print("Hello " + name)


def main():
    # 初始化一个线程，参数传递和使用 Process 一样
    t = threading.Thread(target=hello, args=("shiyanlou",))

    # 启动线程和等待线程结束，和 Process 的接口一样
    t.start()
    t.join()
    print("main thread: {}".format(threading.get_ident()))


if __name__ == "__main__":
    main()
