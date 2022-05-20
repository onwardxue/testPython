# -*- coding:utf-8 -*-
# @Time : 2022/5/18 12:02
# @Author : BinBin Xue
# @File : 025_流程控制语句
# @Project : testPython

# 1. if 关键字的语句结构
# if 判断条件
# if下面的语句用一个tab键或四个空格
age = 19
if age > 18:
    print('你可以开车了')

# if练习
age = input("请输入您的年龄：")
if int(age) > 18:
    print("您成年了，可以去网吧了")

# 2.if else关键字的语句结构
# if 判断条件:
#       判断条件为true时执行的代码
# else:
#       判断条件为else的时候执行的代码

age = 19
if age > 18:
    print('您可以去网吧了！')
else:
    print('回家写作业去！')

# if else练习
age =int(input('请输入您的年龄'))

if age > 18:
    print("欢迎光临")
else:
    print('禁止入内')

# 3.elif关键字的语句
score = int(input("请输入您的成绩"))

if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >=60:
    print(' 及格')
else:
    print("不及格")

# 4.for循环（遍历）
# 格式：for 遍历 in 要遍历的数据：
#               方法体
s = 'china'
for i in s:
    print(i)

# 5. range（左闭右开）
for i in range(5):
    print(i)

for i in range(1,11,3):
    print(i)

