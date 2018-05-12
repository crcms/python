'''

'''

# 字符串列表相互转换

'''
coverList = list('string')
print(coverList)

coverList = list('string')
string = ''.join(coverList)
print(string)
'''

# 列表其它操作
'''
numList = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 赋值
numList[1] = 's'
print(numList)

# 删除
del numList[8]
print(numList)

# 使用切片删除
numList[-1:] = []
print(numList)

# 列表头部追加元素
numList.insert(0,-1)

# 列表指定位置追加元素
numList.insert(2,'2x')
print(numList)

# 删除列表中指定位置的元素
# 默认index不填，则表示最后一个
# pop是list操作中惟一一个有返回值的方法，返回弹出后的值
value = numList.pop()
value2 = numList.pop(-2)
print(numList, value, value2)

# 追加到列表末尾
numList.append('last')
print(numList)

# 清空整个列表
# numList.clear()
# 或
# numList[:] = []

# 列表默认为引用类型，此处使用深复制，只copy内容而非地址
numList2 = numList.copy()
numList3 = numList[:]
print(numList3, numList2, numList)
print('==========================')
numList2[1] = 'x2'
numList3[1] = 'x3'
print(numList3[1],numList2[1],numList[1])

# 切片赋值，一段区间的值重新赋值
numList[0:3] = list('abcd')
numList[-3:] = ['l','a','s','t']
# 增加步长
numList[0:5:2] = list('xyz')
print(numList)

# count，统计元素出现次数
numList.append(0)
count = numList.count(0)
print(count)

# 获取第一个元素的索引位置
print(numList.index(2))

# 指定从指定位置寻找
numList.insert(4, 5)
print(numList)
print(numList.index(5, 5, len(numList)))

# extend
numList2 = list('abc')
# extend将会修改原始列表 而列表相加则会生成一个新的第三方列表，并不修改相加两方的值 
numList.extend(numList2)
print(numList)


# remove 移除指定的第一个元素
numList[-1:] = [2,2,2]
print(numList)
numList.remove(2)
print(numList)

#  反转列表
numList.reverse()
print(numList)

# sort排序
numList[0:6:2] = [10,-1,2]
print(numList)
# sort 只能用于数字
numList.sort()
print(numList)

# sorted函数排序和sort不同，它返回的是一个排序后的副本
numList[0:5:2] = [10,-1,1]
newList = sorted(numList)
print(newList)


# sort自定义高级排序
numList[len(numList):] = [-1,-2,-3]
print(numList)

def adv_sort(value):
    return value

#使用自定义函数来排序
numList.sort(key=adv_sort)
print(numList)
# Bool True倒排
numList.sort(reverse=True)
print(numList)
'''

numList = [0, 1, 2, 3, 4, 5, 6, 7, 8]



#
#
#
#
# numList = [0,1,2,3,4,5,6,7,8]
#
# numList.append(9)
#
# num = numList.pop()
# print(num,numList)
