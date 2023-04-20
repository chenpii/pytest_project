"""
面向对象方式断言
"""
from pytest_assume.plugin import assume

from btest.D2.face_to_object import Person


def test_field_access():
    p = Person('lyf', 22, 170, 50)
    with assume:
        assert p.name == 'lyf'

    with assume:
        assert p.age == 22

    with assume:
        assert p.height == 170

    with assume:
        assert p.weight == 50


class TestEquality():
    def test_person(self):
        # 预期值
        expected_p = Person("lyf", 20, 170, 60)
        # 实际值
        actual_p = Person("lyf", 20, 170, 60)
        assert expected_p == actual_p
