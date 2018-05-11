def func(list):
    list[0] = 'test'
    return list


list = [1, 2, 3]

# list是引用传值，如果直接传入list，里面的值被改掉的话，list本身也会被更改
print(func(list))
print(list)

# 使用[:]可取消list修改

print('=============================')

list2 = [1, 2, 3]
print(func(list2[:]))
print(list2)


### 多参数传递


def func1(test, *tupleParam):
    print(test)
    print(tuple)


# 多个参数使用*会将剩余参数传递到无组中去
func1(123, 'abc', [1, 23], True, 1.23)
print('================')


def func2(**directory):
    for (key, value) in directory.items():
        print('key:' + key + '=====' + 'value:' + value)


func2(a='123', b='456', c='c')
