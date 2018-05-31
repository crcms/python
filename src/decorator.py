# -*- coding: utf-8 -*-

'''



'''



def decorator_test(func):
    '''
    基础的装饰函数
    :param func:
    :return:
    '''
    def wrapped(*args, **kwargs):
        print(args,kwargs)
        print('装饰前')
        result = func(*args, **kwargs)
        print('装饰后')
        return result

    # 返回wrapped作为装饰函数
    return wrapped



'''
@decorator_test
def test(params,**di):
    return params

test({'a':1,'b':2},d=1,x=2)
'''


def test(params,**di):
    return params


decorator_test(test)({'a':1,'b':2},d=1,x=2)

'''

装饰器大概流程

decorator_test带了一个函数名的参数

先执行了decorator_test

decorator_test函数返回了内部定义的wrapped

而wrapped带了参数 (*args,**kwargs)

所以
decorator_test(test) => 相当于wrapped
decorator_test(test)({'a':1,'b':2},d=1,x=2) => 相当于wrapped({'a':1,'b':2},d=1,x=2)

而最后wrapped调用了func函数，并且又用*分拆了参数，传给了func
相当于test({'a':1,'b':2},d=1,x=2)

最后拆开看

decorator_test(test)({'a':1,'b':2},d=1,x=2)
 =>
wrapped({'a':1,'b':2},d=1,x=2)
=>
func(*args,**kwargs) # 自动拆开参数

执行顺序是由左到右

'''

# def abc(name,arg1):
#     return  123
#
#
# d = abc
# print(d('1','1'))