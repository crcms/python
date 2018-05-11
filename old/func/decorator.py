# 定义一个装饰器函数
def log(func):
    def decorator(name):
        print('记录日志')
        func(name)
        print('结束记录日志')

    return decorator


def exec(func):
    def decorator(name):
        print('在执行')
        func(name)
        print('结束执行')

    return decorator


@log
def test(name):
    print('已经在执行')


'''
此处执行顺序如下：
log(test)('abc')
'''


# log(test)('abc')





# test()

@exec
@log
def testParam(name):
    print(name + '已经在执行')


'''
双层装饰器中可以看出先执行靠原函数的，如上先执行log，再执行exec
这里相当于
logDecorator = log(testParam)(name)
然后
execDecorator = exec(logDecorator)(name)
那么整合起来就是
exec(log(testParam))(name)
'''
print('===========解析前============')
testParam('abc')
print('===========解析后============')
# 需要先去掉testParam的装饰参数
exec(log(testParam))('abc')
