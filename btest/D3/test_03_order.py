"""
夹具执行的顺序判断，依次考虑以下
1.范围
    首先执行范围更高的夹具。session > package > module > class > method
2.依赖
    同级别夹具，当B夹具请求A夹具时，首先执行A夹具
3.是否自动
    同级别夹具，自动比非自动先执行

当同级别夹具，既没有依赖关系，也都不是自动夹具，那按照传入的顺序执行。
"""

import pytest


@pytest.fixture(scope="session")
def order():
    return []


@pytest.fixture()  # 不加scope的默认为function
def func_A(order):
    order.append("function_A")


@pytest.fixture()
def func_B(order):
    order.append("function_B")


@pytest.fixture(autouse=True)  # 同级别自动夹具，最先执行。
def func_C(order):
    order.append("function_C")


@pytest.fixture(scope="class")
def cls(order):
    order.append("class")


@pytest.fixture(scope="module")
def mod(order):
    order.append("module")


@pytest.fixture(scope="package")
def pack(order):
    order.append("package")


@pytest.fixture(scope="session")
def sess(order):
    order.append("session")


class TestClass:
    def test_order(self, func_B,func_A, cls, mod, pack, sess, order):  # 传入的夹具是无序的
        assert order == ['session', 'package', 'module', 'class', 'function_C', 'function_A', 'function_B']
