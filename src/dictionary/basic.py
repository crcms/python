'''

字典的基本使用


# 创建一个字典

cd1 = {
    0.01:'x',
    1:'y',
    'key':'value'
}
cd2 = dict(name='simon',age=20)
cd3 = dict([('key1','key2'),('value1','value2')])

print(cd1,cd2,cd3)



d = dict(name='simon', age=20)

# 获取字典长度
print(len(d))


# 获取value值
print(d['name'])
print(d.get('age'))
print(d.get('non'))


# 删除指定key
del d['name']
print(d)


# 修改值
d['name'] = 'hello'
print(d)


# 判断字典中是否存在此key
print('name' in d)
print('x' in d)


# 字符串使用字典格式化
print("my name is {name},my age is {age}".format_map(d))


# 清空字典
# 普通赋值清除，则只会清除当前字典，如果是clear，则会清除所有赋值前的
d2 = d1 = d
d['x'] = '123'
print(d,d1)
d = {}
print(d1)


# 浅复制 copy()
d1 = d.copy()

d1['name'] = 'hello'
d1.get('attributes').remove('footer')
d1['attributes'] = ['face']

# 如果d1不是强硬复制，而使用remove等引用操作则原件也会受到影响
print(d1,d)

# 所以使用如下深复制
from copy import deepcopy

d = dict(name='simon', age=20, attributes=['face', 'head', 'footer'])

d1 = deepcopy(d)
d1['name'] = 'hello'
d1.get('attributes').remove('footer')
print(d1,d)


# fromkeys 创建一个所有值都为None的字典
print({}.fromkeys(['name','age']))


# items 返回一个列表，每个元素都是字典(key,value)形式的元组
print(d.items())


# keys 获取字典所有的key
print(d.keys())


# values 获取字典所有的value
print(d.values())


# setdefault()，在字典key不存在的情况下设置一个默认值
d.setdefault('name','abc')
print(d['name'])
d.setdefault('s',123)
print(d['s'])


#pop删除字段中指定的key
attributes = d.pop('attributes')
print(attributes,d)


# popitem 随机弹出字典项
item = d.popitem()
print(item,d)
'''

d = dict(name='simon', age=20, attributes=['face', 'head', 'footer'])

# update 使用指定字段值更新一个已存在的字典
# 其实基本上就是Merge
d1 = {
    'name': 'abc',
    'test': 123
}

d.update(d1)
print(d)