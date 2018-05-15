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
        print('装饰前')
        result = func(*args, **kwargs)
        print('装饰后')
        return result

    # 返回wrapped作为装饰函数
    return wrapped



@decorator_test
def test(params,**di):
    return params



test({'a':1,'b':2},d=1,x=2)