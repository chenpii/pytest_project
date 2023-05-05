'''
动态指定夹具的作用范围
概念：用命令行选项指定夹具scope的范围，让夹具提供的资源，缩小范围或让范围变得更广，符合我们特定的需求场景。
目的：不更改代码的情况下更改夹具的范围
'''
import pytest


def pytest_addoption(parser):  # parser 参数对象
    # step1 添加命令行参数 --scope
    parser.addoption(
        "--scope",
        action='store',  # 默认存储方式，存储参数的值
        default='function',  # 默认值
        choices=('session', 'package', 'module'),  # 选项
        help="my option：session or package or module"  # 帮助提示
    )


# step2 封装控制scope范围的函数
# pytest会识别，将config获取的范围传递给fixture_name 即对应夹具的名字
def dynamic_scope(fixture_name, config):
    # 如果--scope 选项值是session，则返回session
    if ('session' in config.getoption("--scope", None)):
        return 'session'
    # 如果--scope 选项值是package，则返回package
    elif ('package' in config.getoption("--scope", None)):
        return 'package'
    # 如果--scope 选项值是module，则返回module
    elif ('module' in config.getoption("--scope", None)):
        return 'module'
    # 返回函数级
    else:
        return 'function'


# step3 将夹具的scope参数值替换成封装好的动态函数名
@pytest.fixture(scope=dynamic_scope)
def student():
    return []
