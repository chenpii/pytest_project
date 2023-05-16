'''
并发测试

pytest-xdist插件，用于分布式测试和故障循环测试。

例如：某个参数化测试用例执行时，有大量的参数化数据，如果一条条按顺序执行，特别慢而且浪费时间。可以使用 pytest-xdist，让自动化测试用例可以分布式执行，节省时间。


分布式执行用例的原则：

用例之间是相互独立的，没有依赖关系，完全可以独立运行；
用例执行没有顺序要求，随机顺序都能正常执行；
每个用例都能重复运行，运行结果不会影响其他用例。
'''

import pytest
from time import sleep

# def test_demo_1():
#     sleep(10)
#     assert True
#
# def test_demo_2():
#     sleep(10)
#     assert True
#
# def test_demo_3():
#     sleep(10)
#     assert True


@pytest.mark.parametrize("n", list(range(30)))
def test_demo_param(n):
    sleep(2)
    assert True