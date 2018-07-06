import random
from fractions import Fraction
from sys import getrefcount

#region 面试知识点测试3  Python知识点汇总

#region 判断素数
def primeNum():
    #接收用户输入值
    try:
        n = int(input("please enter the number："))

        if n == 1:
            print(" %d is not a prime number！" % n)
        elif n > 0:
            num = 0
            if int(n / 2) <= 2:
                num = n
            else:
                num = int(n / 2)

            for i in range(2, num):
                if n % i == 0:
                    print(" %d is not a prime number！" % n)
                    break
            else:
                print(" %d is a prime number！" % n)
        else:
            print("输入错误，请输入正整数！")

    except:
        print("输入错误，请输入正整数！")



#endregion

#region 台阶问题 斐波那契
def fbnq():
    fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
    print(fib(4))

#endregion

#region 创建字典
def credict():
    items = [('name', 'earth'), ('port', '80'),('zz', '32')]
    dict2 = dict(items)
    dict1 = dict((['name', 'earth'], ['port', '80'],['ss', '43']))
    print(dict2)
    print(dict1)

#endregion

#region 二分查找
def binarySearch(l, t):
    low, high = 0, len(l) - 1
    while low < high:
        print (low, high)
        mid = int((low + high) / 2)
        if l[mid] > t:
            high = mid
        elif l[mid] < t:
            low = mid + 1
        else:
            return mid
    return low if l[low] == t else False

def erfen():
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    print (binarySearch(l, 12))
    print (binarySearch(l, 1))
    print (binarySearch(l, 13))
    print (binarySearch(l, 444))

#endregion

#region 快排
def qsort(seq):
    # print(seq)
    if seq==[]:
        return []
    else:
        pivot=seq[0]
        lesser=qsort([x for x in seq[1:] if x<pivot])
        # print(lesser)
        greater=qsort([x for x in seq[1:] if x>=pivot])
        # print(greater)
        return lesser+[pivot]+greater

def qs():
    seq=[5,6,78,9,0,-1,2,9,3,-65,12]
    print(qsort(seq))
#endregion

#region 找零问题
def  coinChange(values, money, coinsUsed):
    #values    T[1:n]数组
    #valuesCounts   钱币对应的种类数
    #money  找出来的总钱数
    #coinsUsed   对应于目前钱币总数i所使用的硬币数目
    for cents in range(1, money+1):
        minCoins = cents     #从第一个开始到money的所有情况初始
        for value in values:
            if value <= cents:
                temp = coinsUsed[cents - value] + 1
                if temp < minCoins:
                    minCoins = temp
        coinsUsed[cents] = minCoins
        print('面值为：{0} 的最小硬币数目为：{1} '.format(cents, coinsUsed[cents]) )

def getcoin():
    values = [ 25, 21, 10, 5, 1]
    money = 63
    coinsUsed = {i:0 for i in range(money+1)}
    # print(coinsUsed)
    coinChange(values, money, coinsUsed)
#endregion



#region  广度遍历和深度遍历二叉树
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

## 15 层次遍历
def lookup(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print (current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
## 16 深度遍历
def deep(root):
    if not root:
        return
    print (root.data)
    deep(root.left)
    deep(root.right)
#endregion

#region
def sortlist():
    l1 = [2,6,3]
    l2 = [4,9,1]
    l3 = l1 + l2
    l3.sort()
    print(l3)
#endregion

#region
def tt1():
    num = 32443
    numstr = str(num)
    lenth = len(numstr)
    print(lenth)
#endregion


#endregion

if __name__ == '__main__':
    # primeNum()
    # fbnq()

    # credict()
    # erfen()
    # qs()
    # getcoin()
    # lookup(tree)
    # deep(tree)
    # sortlist()
    tt1()
