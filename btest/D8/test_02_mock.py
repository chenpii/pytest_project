import pytest
from pytest_assume.plugin import assume

from btest.D2.face_to_object import Person

p = Person("刘亦菲", 18)


def test_cook():
    assert p.cook()['result'] == '酸辣土豆丝'


def test_eat():
    with assume:
        assert p.eat('西红柿炒鸡蛋')['status'] == '太好吃'
    with assume:
        assert p.eat('虾仁西蓝花')['status'] == '还可以'
    with assume:
        assert p.eat('酸辣土豆丝')['status'] == '还不错'
    with assume:
        assert p.eat('臭豆腐')['status'] == 500


eat_status = [
    ('西红柿炒鸡蛋', '太好吃'),
    ('虾仁西蓝花', '还可以'),
    ('酸辣土豆丝', '还不错'),
    ('臭豆腐', 500)

]


# 参数化装饰器
@pytest.mark.parametrize('food,status', eat_status)
def test_eat_param(food, status):
    assert p.eat(food)['status'] == status
