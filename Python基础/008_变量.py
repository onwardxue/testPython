# -*- coding:utf-8 -*-
# @Time : 2022/5/18 9:58
# @Author : BinBin Xue
# @File : 008_变量
# @Project : testPython

# 1.变量的格式：变量的名字 = 变量的值
weather = "今天的天气很好，晴天了！"
print(weather)

# 应用场景
img = 'http:www.hello.world'
print(img)

# 2.变量类型：数值(int float) 布尔(boolean) 字符串(string) 列表(list) 元组(tuple) 字典(dict)

# 数值
# int
money = 5000
# float
money1 = 1.2

# 布尔
# 流程控制语句
# 性别的变量
# 性别在实际的企业级开发中，使用的单词是sex和gender
# 男 True
sex = True
gender = False

# 字符串
s = '你是我的小苹果'
s1 = "滴答滴答"

# 列表（放很多变量）
name_list = ['周杰伦' , '科比']
print(name_list)

# 元组（和列表基本一样）
age_tuple = (18,19,20)
print(age_tuple)

# 字典 （scrapy框架使用）
# 格式：变量的名字 = {key:value, key1:value1}
person = {'name': '红浪漫', 'age': 18}
print(person)

# 3.查看数据类型 - type（变量没有类型，数据才有类型）
a = 1
print(type(a))

# 4.变量的命名规范
# 数字不能开头
# 严格区分大小写
# 不能使用关键字
# 标识符命名要做到顾名思义，遵守一定的规范
# 命名法：小驼峰（主要）、大驼峰、下划线连接

# 5.变量的类型转换 - 转换失败的原因：字符串中包含了非法字符
x = 1.9
print(type(int(x)))     # 字符串转整型
print(type(float(x)))   # 字符串转浮点型
print(type(str(x)))     # 整型转字符串，用于拼接
print(type(bool(x)))    # 数值型除了0都是True;字符串/列表/元组/字典中有内容就是True
