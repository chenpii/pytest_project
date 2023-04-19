"""
中级自定义装饰器
"""


def say_middle(func):
    # 装饰函数
    def wrapFunction():
        print("说话之前")
        say_style = func()
        print("说话完毕")
        return say_style

    return wrapFunction


@say_middle
def say_People():
    print("我是say_People")


# 因为say_People 头上装饰了say_middle
# 在调用say_People 时候对say_People自动进行装饰
say_People()

# 当我们想知道当前执行的是哪个被装饰过的函数
print(say_People.__name__)  # 打印的是warpFunction，改变了函数本身的属性
# 为了解决优化，改进装饰器
