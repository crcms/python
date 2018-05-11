'''
列表的基础操作，分片，删除，复制，修改
'''

# 通用的序列操作

list = [0, 1, 2, 3, 4, 5, 6, 7]

# 切片
# 其中第一个索引指定的元素包含在切片内，但第二个索引指定的元素不包含在切片内
# 第二个索引是切片后余下的第一个元素的编号,索引-1
list1 = list[0:5]
list2 = list[1:3]
print(list1, list2)

print('=========================')

# 前后元素值
print(
    list[:3],
    list[-3:]
)

print('=========================')

# 步长
print(
    list[0:4:2],
    list[-4::2],
    list[-4::-2]
)
print('=========================')

# 相加
x = [1, 2, 3]
y = [4, 5, '6']
print(x + y)

'''
乘法 (就是repeat)
x = [1, 2, 3]
y = [4, 5, '6']
print((x + y) * 2)
result:[1, 2, 3, 4, 5, '6', 1, 2, 3, 4, 5, '6']
'''

'''
判断元素是否在列表中
y = [4, 5, '6']
print('6' in y, 6 in y)

#二级元素列表
bigList = [['name',12],['name2',13]]
print(['name',12] in bigList,['name3',13] in bigList)
'''

'''
#len
x = [0,1,2,3]
print(len(x))
#max
print(max(x))
#min
print(min(x))
'''

print('=========================')

string = 'string'
print(string[0])
