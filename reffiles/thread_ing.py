import threading
import time


def fun1():
    # 可以换成udp接收数据的函数
    for i in range(4):
        print("func1 running\n")
        time.sleep(1)


def fun2(ras):
    # 可以换成udp发送数据的函数
    for i in range(ras):
        print("func2 running\n")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2, args=(6,))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
