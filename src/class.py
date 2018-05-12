'''


'''


class Parent:

    def __init__(self):
        pass

    def func(self, age=123):
        return age


class Parent2:
    def __init__(self):
        pass

    def func(self, name='abc'):
        return name


class Son(Parent, Parent2):
    pass


# 判断子类是否属于父类
print(issubclass(Son, Parent))

# 判断实例是否属于某个类
son = Son()
print(isinstance(son, Son))

# 判断方法是否存在
print(hasattr(son, 'func1'), hasattr(son, 'func'))

print(type(son))



# 抽像类
from abc import ABC,abstractmethod

class D(ABC):

    @abstractmethod
    def b(self):
        pass

D()