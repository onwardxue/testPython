# -*- coding:utf-8 -*-
# @Time : 2022/5/18 16:28
# @Author : BinBin Xue
# @File : 047_文件
# @Project : testPython

# 1.文件的打开与关闭
# 打开文件/创建文件
# open(文件的路径，模式）
# 模式：w 可写；r 可读
# 文件路径：绝对路径、相对路径
fp = open('test.txt', 'w')
fp.write('hello,world')
# 文件的关闭
fp.close()

# 2.文件的读写
# 写数据
# 如果模式为w，是覆盖原内容；模式为a，是追加在原内容后面
fp = open('test.txt','a')
fp.write(' hello world\n' * 50)
fp.close()
# 读数据
# 默认情况下，read是一字节一字节的读，效率比较低
fp = open('test.txt','r')
content = fp.read()
print(content)

# readline是一行一行的读取 但是只能读取一行
content = fp.readline()
print(content)

# readlines可以按照行读取，但会将所有数据都读取到并且以一个列表的形式返回，而列表的元素是一行一行的数据
content = fp.readlines()
print(content)

# 3.文件的序列化和反序列化
# 默认情况下，对象是无法写入到文件中，如果想将对象写入到文件，那么必须使用序列号操作（将对象转成字符串）
# 在使用scrapy框架时，会返回一个对象，如果我们要将其写入到文件中，就要使用json.dumps
# 序列化的两种方式dumps()和dump
# dumps()
# （1）创建一个文件
fp = open('test.txt','w')
# （2）定义一个列表
name_list = ['zs','ls']
# （3）导入json模块到该文件中并进行对象序列化
import json
names = json.dumps(name_list)
print(names)
# （4）写入序列化后的变量到文件中
fp.write(names)
fp.close()
# dump 合并dumps的3、4步（序列化 + 写入文件）
json.dump(name_list,fp)
fp.close()

# 反序列化 - 将json的字符串变成一个python对象
# 两种方式：loads和load
fp = open('test.txt','r')
content = fp.read()
import json
result = json.loads(content)
# 转换之后
print(result)
# load 也是将两步合成一步（读取+反序列化）
result = json.load(fp)
