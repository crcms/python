'''

函数的基础使用


# 文档字符串

def document():
    \'''
    document func
    :return: string
    \'''
    pass

print(document.__doc__)



#help 函数打印文档说明
def document():
    \'''
    document func
    :return: string
    \'''
    pass

print(help(document))



# 列表的传值

numList = list(range(0,9))

def document(arg):
    arg[0] = '123'

# 如下列表是传址，所以当函数内更改后原列表值也会被更改
# print(numList)
# print(document(numList))
# print(numList)

# 如果不需要更改原列表值，需要创建完全的副本 copy 或 [:]

print(numList)
# print(document(numList[:]))
print(document(numList.copy()))
print(numList)

# 字典也是一样，需要使用copy来进行深复制
d = dict(key='value', key2='value2')

def document(arg):
    arg['key'] = '123'

print(d)
print(document(d.copy()))
print(d)



# map 函数

numList = list(range(0, 9))

def map_function(item):
    return item + 1

# print(map(map_function, numList))
for x in map(map_function, numList):
    print(x)

print(numList)


# filter过滤函数
numList = list(range(0, 9))

def fil(item):
    return  item>5
print(list(filter(fil,numList)))
print(numList)


# reduce函数
numList = list(range(0, 9))

def red(item1, item2):
    return item1 + item2

# from functools import reduce
import functools
print(functools.reduce(red,numList))


# sum 求合元素
numList = list(range(0, 9))
print(sum(numList))
'''
