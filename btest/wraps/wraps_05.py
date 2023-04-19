"""
带参数的装饰器

定义一个装饰器把返回的字符串改成大写
"""
from functools import wraps


# 装饰器
def to_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        if not isinstance(text, str):
            raise TypeError("输入参数类型有误，不是字符串")
        return text.upper()

    return wrapper


# 被装饰器修饰的函数
@to_uppercase
def say_language(say_str):
    return say_str


language = say_language("speak chinese")
print(language)
