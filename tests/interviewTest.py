import random
from sys import getrefcount

#region 面试知识点测试

#region 用Python输出一个Fibonacci数列
import gc


def Fibonacci():
    a, b = 0, 1

    list = []

    while b<100:

        # print(b)

        a, b = b, a + b

        list.append(b)

    print(list)
#endregion


#region 获取dict中key和value ，format()用法
def keyvaluetest():
    tdict = {'a':1,'b':2,'c':3}

    for k,v in tdict.items():
        print(k)
        print(v)

    print('今天{0}'.format('天气不错'))
    print('{:.1f}'.format(4.234324525254))
    print('{:.4f}'.format(4.1))

#endregion

#region lambda函数用法， 推导式用法
def lambdatest():
    f = lambda x, y: x + y
    f2 = lambda x: [print(a) for a in x if a < 2]

    # print(f(1,3))
    # print(f2([1,3,2]))
    # print([a + 1 for a in [1, 3, 2] if a < 2])

    # strings = ['import', 'is', 'with', 'if', 'file', 'exception']
    strings = {'a':1,'b':2,'c':3}
    # D = {key: val for val, key in enumerate(strings)}
    D = {val: key for key, val in strings.items()}
    f3 = lambda strings:D

    print(f3(strings))
#endregion

#region 冒泡排序
def maopao():
    list = [2,34,78,23,11,0,3]
    leng = len(list)

    for i in range(leng):
        for j in range(leng -i -1):
            a = list[j]
            b = list[j+1]

            if a > b:
                tmp = a
                list[j] = b
                list[j + 1] = tmp


    print(list)

#endregion


#region 引用和对象  ，垃圾回收(garbage collection)
from sys import getrefcount

import objgraph
import gc

def duixiang():
    # 内存地址的十进制表示
    print(id(12))
    print(id(12))
    print(id(1))
    #内存地址的十六进制表示
    print(hex(id(12)))

    #引用计数(reference count)  getrefcount()

    a = [1, 2, 3]

    # b = [a,a]
    b=a


    print(getrefcount(a))

    #拓扑结构
    x = [1, 2, 3]
    y = [x, dict(key1=x)]
    z = [y, (x, y)]


    objgraph.show_refs([z], filename='ref_topo.png')

    #引用环
    # a = []
    # a.append(a)
    # print(getrefcount(a))

    #引用减少 del关键字

    # print(getrefcount(b))

    # del a
    # print(getrefcount(b))

    print(getrefcount(b))

    a = 1
    print(getrefcount(b))


    #通过gc模块的get_threshold()方法，查看该阈值
    print(gc.get_threshold())

    #通过gc中的set_threshold()方法重新设置
    gc.set_threshold(750, 10, 10)

    #手动启动垃圾回收，即使用gc.collect()
    gc.collect()

    # del a[0]
    # print(a)


class from_obj(object):
    def __init__(self, to_obj):

        self.to_obj = to_obj

    # b = [1, 2, 3]
    # a = from_obj(b)
    # print(a.to_obj)
    # print(id(a.to_obj))
    # print(id(b))



#endregion


#region 写一个函数, 输入一个字符串, 返回倒序排列的结果

#利用字符串本身的翻转
def string_reverse1(text='abcdef'):

    print(text[::-1])
    return text[::-1]

# 把字符串变成列表，用列表的reverse函数
def string_reverse2(text='abcdef'):

    new_text = list(text)

    new_text.reverse()

    print(new_text)

    print(''.join(new_text))
    return ''.join(new_text)

#新建一个列表，从后往前取

#利用双向列表deque中的extendleft函数

#递归

#endregion


#region 按升序合并如下两个list, 并去除重复的元素

def listtest():
    list1 = [2, 3, 8, 4, 9, 5, 6]

    list2 = [5, 6, 10, 17, 11, 2]

    # 最简单的方法用set

    list3 = list1 + list2

    # print(set(list3))
    #
    # print(list(set(list3)))
    #
    # print(sorted(list(set(list3))))

    #递归   先选一个中间数，然后一边是小的数字，一边是大的数字，然后再循环递归，排完序

    qsort(list1+list2)

    print(qsort(list1+list2))

def qsort(L):
    if len(L) < 2 :
        return L
    pivot_element = random.choice(L)

    small = [i for i in L if i < pivot_element]
    large = [i for i in L if i > pivot_element]

    return  qsort(small) + [pivot_element] + qsort(large)






#endregion


#region 说出下面list1,list2,list3的输出值
# def extendList(val, list=[]):
def extendList(val, list=None):

    if list is None:
        list = []

    list.append(val)

    return list

def listtest2():
    list1 = extendList(10)

    list2 = extendList(123, [2,'b'])

    list3 = extendList('a')

    print(list1)
    print(list2)
    print(list3)


#endregion


#region 写出你认为最Pythonic的代码
# Pythonic编程风格是Python的一种追求的风格，精髓就是追求直观，简洁而容易读.
def pythonic():
    a= 1
    b =2
    a, b = b, a
    c,d = a,b

    print(a,b)
    print(c,d)

# zip创建键值对
def ziptest():
    keys = ['Name', 'Sex', 'Age']

    values = ['Jack', 'Male', 23]

    print(dict(zip(keys, values)) )
#endregion

#endregion

if __name__ == '__main__':
    # Fibonacci()
    # keyvaluetest()
    # lambdatest()

    # maopao()
    # duixiang()
    # string_reverse2()
    # listtest()
    # listtest2()
    # pythonic()

    ziptest()