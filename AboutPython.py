# 这是我的第一个python代码
print('hello YANcq')
print('''这是多行字符串。\nThis is the second line. \n"what's your name" I asked.\nMy name is "Blue"''')
print('''这是多行字符串。
This is the second line.
"what's your name" I asked.
My name is "Blue"''')
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
# 与上一句输出相同(数字是一个可选项)
print('{} was {} years old when he wrote this book'.format(name, age))
# 对于浮点数'0.33333' 保留小数点后3位
print('{0:.3f}'.format(1.0 / 3))
# 使用^定义填充文本后字符串的长度,^之前的符号代表填充符号
# 下面有3种情况仔细看看
print('{0:+^11}'.format('hello'))
print('{0:_^4}'.format('hello'))
print('{0:?^4}'.format(''))
# print('{0:??^4}'.format('')) 报错
# 基于关键词输出
print('{name} wrote {book}'.format(name='Swaroop', book='A byte of python'))
# print总是会以一个看不见的\n 结尾，因此重复调用print 会在相互独立的一行中相互打印。为了避免出现这个换行符，
# 可以通过end 指定其以空白结尾
print('a', end='')
print('b')
name = input("input your name please:")
print('hello', name)
# 如果需要指定一些未经处理的字符串，比如转义序列，那么需要在字符串前增加r 或 R 来指定一个原始字符串。
str1 = r"Newlines are indicated \n"
print(str1)
# 显式行连接
s = 'This is a string.' \
    'This is a String'
print(s)
# i = \
# 5 等同于 i = 5
# 控制流
a = 5
if a > 3:
    print('bigger than three')
else:
    print('smaller than three')
for i in range(1, 5):
    print(i)
else:
    print('The loop is over')
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    print('The length of {0} is {1}'.format(s, len(s)))
print('Done')


def say_hello():
    print('hello')


say_hello()


def func(m=4, *args, **dicts):
    print('m', m)
    for single_Item in args:
        print('single_Item', single_Item)
    for first_part, second_part in dicts.items():
        print(first_part, second_part)


print(func(10, 1, 3, 4, 5, jack=1112, tom=2223, siri=3334))