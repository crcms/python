'''

bool假比对，其它则为真


# False 0 None {} [] () "" 0.0(浮点型)

if 0.0:
    print('true')
else:
    print('false')


if []:
    print('true')
else:
    print('false')


if () or {}:
    print('true')
else:
    print('false')


# 将其它值转换为bool
print(bool(0.2))


# is来判断两个对象是否相同，即同址

x = y = list('string')
z = list('string')

print(x is y)
print(x is z)
'''
