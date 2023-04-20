def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))



# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Adam', 45, **extra)


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 必选参数

# 默认参数 n=5

# 可变参数 *args

# 命名关键字参数 *，或者*args，之后的参数，限定关键字

# 关键字参数 **kw


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args = ', args, 'kw = ', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd = ', d, 'kw = ', kw)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, 3, d='aaa', ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 99, 'x': '#'}
f2(*args, **kw)
