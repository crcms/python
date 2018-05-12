'''

字符串的内置函数

string = 'string'
# 像两边填充指定长度，字符串+填充长度=指定长度
print(string.center(21,'*'))


# 组合一个列表为字符串
numList = ['a','b','c']
print(''.join(numList))


# 查找字符串第一次出现的位置
print(string.find('r'))
# 未找到则返回-1
print(string.find('x'))


# 转换为大小写
print(string.upper())
print(string.lower())


# 将字符串切分为列表
string = 's+t+ring'
print(string.split('+'))

# 替换
string = 'string'
print(string.replace('i','xxx'))


# 去除两边空白
string = '       string      '
print(len(string.strip()))
'''

string = 'string'



