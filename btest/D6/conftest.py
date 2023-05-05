'''
命令行选项参数的使用场景：

当团队有很多测试环境，每个测试环境都有不用的端或者不同的项目组。
当跑自动化的时候，可以通过命令行进行不同环境的切换，让一份代码跑在不同的环境里面。
'''
import pytest


# 根据命令行选项将不同的值传递给测试函数
@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


# 自定义的命令行参数，方便用户将数据传递给pytest
# 所有的参数都加在pytest_addoption里
def pytest_addoption(parser):  # parser 参数对象
    # 根据命令行选项将不同的值传递给测试函数
    # 往参数对象里添加参数
    parser.addoption(
        "--cmdopt",  # 参数名
        action="store",  # 默认存储方式，存储参数的值
        default="type1",  # 默认值
        help="my option : type1 or type2",  # 帮助提示
        choices=("type1", "type2")
    )
    # https://docs.python.org/3/library/argparse.html#action

    # 命令行选项参数化
    parser.addoption(
        "--stringinput",  # 自定义命令行选项
        action="append",  # 用列表的方式存储参数值
        default=[],  # 默认值

        # 对参数做简要说明
        help="要传递给测试函数的字符串输入列表"
    )


#  命令行选项参数化，可以使用此钩子实现自定义参数化方案
#  收集测试函数时调用的钩子
def pytest_generate_tests(metafunc):
    # 如果有用例请求了stringinput这个夹具
    if ("stringinput" in metafunc.fixturenames):
        # 获取stringinput选项的值，进行参数化
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
