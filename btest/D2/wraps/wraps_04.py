"""
在类中创建装饰器

类和模块都可以用来创建装饰器，Python对装饰器没有限制。

类能当装饰器，是因为Python提供了一个特殊的方法call，意味着类的实例可以当做函数来调用
"""
from functools import wraps


class Say_Super:
    def __call__(self, func):
        @wraps(func)
        def wrapFunction():
            print("说话之前")
            say_style = func()
            print("说话完毕")
            return say_style

        return wrapFunction

@Say_Super()
def say_Code():
    print('我是say_Code')

say_Code()
