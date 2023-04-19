"""
初级自定义装饰器
"""
def say_Chinese():
    return 'I am say Chinses'


def say_English():
    return 'I am say English'


def say(func):
    return func()


print(say(say_English))