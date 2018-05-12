'''

字符串的格式化


# 基础格式化
raw = 'my name is %s , my age %s \n number %.3f'
value = ('simon',20,0.00312)

# 使用%来组合格式化字符串占位
print(raw % value)



# 字符串模板格式化

from string import Template

tpl = Template("Hello $who, Good !")
string = tpl.substitute(who = 'simon')
print(string)

# 索引格式化
string = "hello {1}, good {0}"
print(string.format('morning','simon'))

# 函数key=>value格式形式化
string = "hello {name}, good {time}"
print(string.format(name='simon',time='morning'))
'''




