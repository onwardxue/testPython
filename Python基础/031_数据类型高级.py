# -*- coding:utf-8 -*-
# @Time : 2022/5/18 13:44
# @Author : BinBin Xue
# @File : 031_数据类型高级
# @Project : testPython

# 1.字符串高级
# 获取长度:len
# 查找内容:find
# 判断头/尾:startswith,endswith
# 计算出出现次数:count
# 替换内容:replace
# 切割字符串:split
# 修改大小写:upper,lower
# 空格处理:strip
# 字符串拼接:join 这个有问题不要用
s = 'china'
print(len(s))
print(s.find('a'))
print(s.startswith('c'))
print(s.endswith('b'))
print(s.count('a'))
print(s.replace('c','d'))
print(s.split('i'))
print(s.upper())
print(s.lower())
print(s.strip())

# 2.列表高级
# 添加:append
# 插入:insert
# 添加列表:extend
food_list = ['小鸡炖蘑菇','蚂蚁上树']
food_list.append('糖醋里脊')
food_list.insert(1,'蘑菇汤')
food_list2 = ['馄饨','拉面']
food_list.extend(food_list2)
print(food_list)

# 修改:直接通过下标修改
food_list[3] = '牛排'
print(food_list)

# 查询元素:in / not in
food = input('请输入你想吃的食物：')
if food in food_list:
    print("在")
else:
    print("不在")

# 删除元素:
# del:根据下标删除
# pop:删除最后一个元素
# remove: 根据元素值删除
a_list = [1,2,3,4,5]
del a_list[2]
print(a_list)
a_list.pop()
print(a_list)
a_list.remove(3)
print(a_list)

# 3.元组高级（元组与列表的区别在于 1.元组元素不能修改 2.元组中的元素只有一个时必须在后面加逗号）

# 4.切片（左闭右开）
s = "hello world"
print(s[0:4])
print(s[1:])
print(s[:4])
print(s[0:5:2])

# 5.字典高级
# 查询
# 获取字典中不存在的key时，会发生异常;使用.get方式获取不会发生异常
# 不能使用.的方式访问字典的数据
person = {'name': '吴铅', 'age' : 29}
print(person['name'])
print(person['age'])
print(person.get('sex'))
# 修改
person['name'] = '法外狂徒'
# 添加
# 如果使用变量名字['键'] = 数据时，这个键如果在字典中不存在，那么就会变成新增元素
person = {'name' : '马冬梅'}
person['age'] = '18'
person['name'] = '罗斯福'
print(person)
# 删除
# del 删除字典中的某一个元素；或删除整个字典
# clear 清空字典但保留字典对象
del person['age']
person.clear()
del person

# 6.遍历
person = {'name' : '老马' , 'age' : 18, 'sex' : '男'}
# 遍历字典的key
for key in person.keys():
    print(key)
# 遍历字典的value
for value in person.values():
    print(value)
# 遍历字典的key和value
for key,value in person.items():
    print(key,value)
# 遍历字典的项/元素
for item in person.items():
    print(item)


