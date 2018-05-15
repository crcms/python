# -*- coding: utf-8 -*-

'''

基础迭代器(iterate)

'''


class Iterate(object):
    _items = []
    _index = 0

    def __init__(self, items):
        self._items = items

    def __next__(self):
        '''
        提供下一个值
        :return: int
        '''

        # 当指针超过下标时，必须抛出StopIteration
        if len(self._items) <= self._index:
            raise StopIteration

        item = self._items[self._index]

        self._index +=1

        return item

    def __iter__(self):
        '''
        提供自身作为iterator 对象
        :return: self
        '''

        return self


if __name__ == '__main__':

    for item in Iterate([1,2,3,4]):
        print(item)
