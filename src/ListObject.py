'''

ListObject测试

'''


class ListObject():
    _items = [1, 2, 3]

    def __init__(self):
        print('初始化')

    def __del__(self):
        # 对象被销毁（作为垃圾被收集）前被调用
        print('析构方法')

    def __len__(self):
        '''
        如果是
        列表，则作为列表长度返回
        字典，则是键值对数
        __len__返回零（且没有实现覆盖这种行为的__nonzero__），对象在布尔上下文中将被视为假
        :return: int
        '''
        return 10

    def _check_index(self, item):
        '''
        检查索引正确性
        :param item: int
        :return: bool
        '''
        if not isinstance(item, int):
            raise TypeError('Item type error')

        # 这里只是示例，其实不完全正确，当是负数的时候
        if len(self._items) >= abs(item):
            return True

        raise IndexError('Index error')


    def __getitem__(self, key):

        if self._check_index(key):
            return self._items[key]


    def __setitem__(self, key, value):

        if not isinstance(key, int):
            raise TypeError

        self._items.insert(key, value)


    def __delitem__(self, key):

        if self._check_index(key):
            del self._items[key]
            print(self._items)


    def __iter__(self):
        '''
        迭代list
        :return: self
        '''
        for item in self._items:
            yield item

listObject = ListObject()

# 当使用len函数其实是调用__len__方法
# print(len(listObject))


# get item
# print(listObject[-1])
# 非数字则为报出类型错误
# print(listObject['s'])
# 下标越界
# print(listObject[10])


# set item
# listObject[10] = 123
# print(listObject)
#
# # del itme
# del listObject[1]


# iterator
# for x in listObject:
#     print(x)


import sys
print(sys.modules)