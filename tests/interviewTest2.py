import random
from fractions import Fraction
from sys import getrefcount

#region 面试知识点测试2  Python知识点汇总

#region 类型和运算

#region 1.1 寻求帮助
from tests.apitest2 import Client

def func1():
    dir(Client)  # 简单的列出对象obj所包含的方法名称，返回一个字符串列表
    print(dir(isinstance))
    help(isinstance)  # 查询obj.func的具体介绍和用法
#endregion

#region 数字的表达式操作符
def func2():
    x = 99
    y =3

    print(x << y)
    print(x >> y)
#endregion

#region 索引、分片、调用
def func3():
    x = 'string'
    i = 1
    j = 4
    k = 2
    print(x[i])
    print(x[i:j:k])
    print(x[:-1])
    print(x[::-3])

    x = Fraction(4,6)
    print(x)

    # print(x(3))
#endregion

def logic1():
    primenumber = []
    i =15
    if i in primenumber :
        print(i)

#endregion




#endregion

if __name__ == '__main__':
    pass

    func3()