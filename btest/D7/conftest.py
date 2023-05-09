import pytest


# step 1： 添加自定义选项--runslow。进行布尔控制控制我们的程序。
def pytest_addoption(parser):
    parser.addoption(
        '--runslow',
        action='store_true',  # 如果出现参数，就保存为true
        default=False,
        help="run sloq test"
    )


# 说明：  不添加此选项时，默认值为False时（执行skip跳过程序，跳过带有slow标签的用例），添加--runslow 即为True,为True 时，执行所有用例。
# 相反action参数：store_false

# step 2：注册标签
# 方式一：在pytest.ini 配置文件markers选项中添加加slow 标记
# 方式二：使用下方钩子函数，进行注册标签。
# def pytest_configure(config):
#     config.addinivalue_line("markers", "slow: mark test as slow to run")


# step 3 : 实现跳过带有标记slow的用例
# pytest_collection_modifyitems 是在用例收集完毕之后被调用，有3个参数，分别是
# session 会话对象
# config 配置对象
# items 用例对象列表
def pytest_collection_modifyitems(config, items):
    print('\n-----------------------')
    print(config)
    print('\n-----------------------')
    # 如果--runslow 在命令行选项中: 不要跳过任何标签
    if config.getoption("--runslow"):
        return

    # --runslow 没有在命令行选项中
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        # 把标签中带有slow关键字的用例，添加到skip_slow中
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
