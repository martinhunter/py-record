import multiprocessing
import time


def fun1():
    for i in range(4):
        print("func1 running\n")
        time.sleep(1)


def fun2(ras):
    for i in range(ras):
        print("func2 running\n")
        time.sleep(1)


def main():
    t1 = multiprocessing.Process(target=fun1)
    t2 = multiprocessing.Process(target=fun2, args=(6,))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
