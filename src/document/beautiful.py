from bs4 import BeautifulSoup
from re import compile

'''

html文档获取

'''

#
soup = BeautifulSoup(markup=open('./test.html',encoding='UTF8'),features='html5lib')

# beautiful也可以看成是一个tag对象
# print(soup.name)
# print(soup.attrs)

# 标签的获取
# soup.[tag]即可
# print(soup.title)


# 获取标签名称和属性
# print(soup.title.name)
# print(soup.title.attrs)
#
#
# # 获取tag内容
# print(soup.title.string)
# print(type(soup.title.string))

# 获取内容和子集

# contents是返回一个列表
# print(soup.head.contents)

# children 返回一个生成器，用于标签循环
# for x in soup.head.children:
#     print(x)


# 文档树的执行

result = soup.find_all(['a'],href=compile(r'^http.*'))
print(result)