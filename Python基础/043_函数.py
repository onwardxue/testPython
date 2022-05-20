# -*- coding:utf-8 -*-
# @Time : 2022/5/18 16:07
# @Author : BinBin Xue
# @File : 043_函数
# @Project : testPython

# 很多重复的业务逻辑，我们可以使用函数

# 1.函数的定义和调用
# 定义
def f1():
    print("欢迎光临")
    print('男宾2位')
    print('欢迎下次光临')
# 调用
f1()


# 2.函数的参数
def sum1(a, b):
    c = a + b
    print(c)
# 位置参数：按照位置一一对应的关系来传递参数
sum1(2, 3)
sum1(100, 200)

# 关键字传参：
sum1(b=200, a=300)


# 3.函数返回值
# 返回值的关键字是return，存在函数中
def buyIceCream():
    return '冰激凌'
print(buyIceCream())


# 4.局部变量和全局变量
# 局部变量：在函数内部定义的变量，其作用域范围是函数内部，函数外部不可以使用
# 全局变量：在函数外部定义的变量，其在函数内部、外部都可以使用
# 在满足条件的情况下，尽量使用作用域最小的变量范围
def f1():
    a = 1
