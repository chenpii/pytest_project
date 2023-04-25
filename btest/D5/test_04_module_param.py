'''
模块全局化参数

当参数在模块范围内共享
'''

import pytest

# 模块全局性装饰器
pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])


def test_add(n, expected):
    assert n + 1 == expected


class TestClass():
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
