"""
改进装饰器
"""

from functools import wraps


# 为了不改变被装饰过函数或类的性质，添加function.wrap装饰器
def say_high(func):
    @wraps(func)
    def wrapFunction():
        print("说话之前")
        say_style = func()
        print("说话完毕")
        return say_style

    return wrapFunction


@say_high
def say_People():
    print("我是say_People")


say_People()

print(say_People.__name__)  # 打印的是say_People
