# -*- coding: utf-8 -*-

'''

内容插槽

'''

class Test(object):

    _width = 10

    @property
    def width(self):
        return self._width


    @width.setter
    def width(self,value):
        self._width = value
        return self


test = Test()
print(test.width)
test.width = 100
print(test.width)