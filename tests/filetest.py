
#region 文件读取
#  这个函数接受文件夹的名称作为输入参数，
#     返回该文件夹中文件的路径，
#     以及其包含文件夹中文件的路径。
import random

import sys

import requests


def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


#endregion


def listtest():
    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    # A0 = {'a': 1, 'c': 3, 'e': 5, 'd': 4, 'b': 2}
    A1 = range(10)
    A2 = [i for i in A1 if i in A0]
    A3 = [A0[s] for s in A0]
    A4 = [i for i in A1 if i in A3]
    A5 = {i: i * i for i in A1}
    A6 = [[i, i * i] for i in A1]

    for s in A0:
        print(s)
    print(type(A0))

    print(A0)
    print(A1)
    print(A2)
    print(A3)
    print(A4)
    print(A5)
    print(A6)


def f(*args,**kwargs): print(args, kwargs)


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

def cProfiletest():
    import cProfile
    # lIn = [1]
    lIn = [random.random() for i in range(100000)]
    cProfile.run('f1([random.random() for i in range(100000)])')
    cProfile.run('f2([random.random() for i in range(100000)])')
    cProfile.run('f3([random.random() for i in range(100000)])')
    print(sys.getrefcount(lIn))

def tupletest():
    t = ('a',1,3)
    print(type(t))
    l = list(t)
    print(l)
    print(type(l))

def sorttest():
    a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]

    a.sort()

    last = a[-1]

    for i in range(len(a) - 2, -1, -1):

        if last == a[i]:

            del a[i]

        else:
            last = a[i]

            print(a)

def f():
    global x
    x = 2

def f2():
    f()
    print(x)

def randomtest():
    print(random.randrange(1, 20, 2))

if __name__ == '__main__':
    pass
    # print_directory_contents('E:\\test2')
    # listtest()
    # cProfiletest()
    # tupletest()
    # sorttest()
    # randomtest()
    # f2()

    data = requests.get('http://shopee.tw/api/v1/category_list/').text
    print(data)

