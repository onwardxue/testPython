# -*- coding:utf-8 -*-
# @Time : 2022/5/18 11:14
# @Author : BinBin Xue
# @File : 017_运算符
# @Project : testPython

# 1.算术运算符：+、-、*、/、//、%、**
a = 3
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 扩展：
# 字符串的加法是进行拼接的，不做运算
# 下面这个会报错，因为Python中不支持数值自动转成字符串
a = '123'
b = 456
print(a + b)
# 字符串的乘法是将字符串重复多次

# 2.赋值运算符： =
# 支持连续赋值
b = c = 2
# 支持多变量赋值（用逗号分割）
d,e,f = 1,2,3

# 3.复合赋值运算符
a = 2
a += 2
a *= 2
a -= 2
a /= 2
a //= 2
a %= 2
a **= 2
print(a)

# 4.比较运算符（返回的都是bool类型的数据）
a = 10
b = 5
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# 5.逻辑运算符（and or not）
print(10 > 20 and 11 > 10)
print(10 > 20 or 11 > 10)
print(not (11 > 10))

# 6.逻辑运算符性能优化
# and性能优化 - 短路与
# 当and前面的是true时才会执行后面的句子，否则不执行
a = 36
a > 10 and print("hello world")
a < 10 and print("hello world")
# or性能优化 - 短路或
# 当or前面的是false时才会执行后面的句子，否则不执行
a = 38
a > 39 or print('你好世界')

