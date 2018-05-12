'''

python 正则



pattern = re.compile(r'\d+[^\d]*\d+')

# match，匹配字符串的开头(必须是起始位置)，如果无法匹配或者到达末尾则返回None
string = '123fdadfa123'
result = re.match(pattern,string)
print(result)
print(result.group())

string = 's123fdadfa123'
result = re.match(pattern,string)
print(result)


# search 和match类似，只不过search会扫描查找整个字符串，并非必须要从头开始匹配
string = 's123fdadfa123'
result = re.search(pattern,string)
print(result.group())

'''

import re


# 分组模式
pattern = r'(?P<num>\d+)[^\d]+(?P=num)'

# 将字符串转换为匹配模式
pattern = re.compile(pattern,re.I | re.M)

_match = re.search(pattern,'x3333fdsa3333')
print(_match.group())
print(_match.groups())
print(_match.lastgroup)
print(_match.start())
print(_match.end())
print(_match.span())

# 匹配开头
pattern1 = r'\Aabc'

# 匹配结束
pattern2 = r'abc\Z'
