"""
捕获详细异常信息，可以用于输出到日志文件、测试报告中
1.获取用例所在模块
2.获取用例的名称
3.获取用例的具体错误信息包
"""
import inspect  # 从实时 Python 对象中获取有用的信息

import pytest


# python-inspect 捕获详细异常信息
def test_inspect_info():
    # 期望值为 模块名::用例名::错误信息
    expected = 'test_06_get_error::test_inspect_info::division by zero'

    with pytest.raises(Exception) as exc_info:
        c = 2 / 0

    # 获取错误文本：exc_info.value.args[0]
    # 如获取错误类型: exc_info.type
    error_info = exc_info.value.args[0]  # 获取用例具体错误信息

    module_name = inspect.getmodulename(__file__)  # 获取用例所在模块
    method_name = inspect.stack()[0][3]  # [0][3]获取用例名字，[1][4][0] 获取用例名字和参数

    actual = f'{module_name}::{method_name}::{error_info}'
    assert expected == actual


# pytest 内置功能捕获异常信息
# request是pytest提供的内置夹具，可以以参数的形式使用
def test_get_raises(request):
    # 期望值为 模块名::用例名::错误信息
    expected = 'test_06_get_error::test_get_raises::division by zero'

    with pytest.raises(Exception) as exc_info:
        c = 2 / 0

    error_info = exc_info.value.args[0]
    module_name = request.module.__name__.split('.')[-1]  # 模块名称
    method_name = request.function.__name__  # 获取用例名字

    actual = f'{module_name}::{method_name}::{error_info}'
    assert expected == actual
