"""
自定义辅助断言函数

好处：让用例跟断言语句进行分离,把一些复杂的验证逻辑封装到函数里。使得用例的可读性更强
"""
import pytest

from btest.D2.face_to_object import Person


def assert_identical(p1, p2):
    if (p1.name != p2.name):
        pytest.fail(f"name 不匹配：{p1.name} != {p2.name}")


def test_identical():
    p1 = Person("lyf", 18, 170, 60)
    p2 = Person("ym", 18, 170, 60)
    assert_identical(p1, p2)
