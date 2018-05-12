'''

异常


# 抛出异常
raise Exception('Base Exception')
'''



# 捕获异常

try:
    x = 10
except ZeroDivisionError:
    x = 5
    if x == 10:
        raise ValueError
    else:
        raise


# 捕获多个异常对象
try:
    pass
except (ZeroDivisionError, Exception) as e:
    print(type(e))
    pass


# 捕获所有异常
try:
    pass
except:
    pass


# else使用

try:
    pass
except:
    pass
else:
    print('no exception')


# finally

try:
    pass
except NameError:
    pass
else:
    pass
finally:
    print('都执行')