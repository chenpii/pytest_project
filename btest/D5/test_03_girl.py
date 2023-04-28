import random

import pytest
from faker import Faker

from btest.D2.face_to_object import Person


# 随机创建虚拟对象
def create_girl(numbers: int, list_person=[]):
    fake = Faker('zh_CN')
    for i in range(numbers):
        girl_name = fake.name_female()  # 女性名字
        girl_age = random.randint(18, 25)  # 年龄
        girl_height = random.randint(165, 175)  # 身高cm
        girl_weight = random.randint(45, 60)  # 体重kg
        gf = Person(girl_name, girl_age, girl_height, girl_weight)
        list_person.append(gf)

    return list_person


# 辅助断言函数
def assert_help(person: Person):
    return (
            18 <= person.age <= 25 and
            165 <= person.height <= 175 and
            45 <= person.weight <= 60
    )


persons = create_girl(5)
person_ids = [f"{p.name}-{p.age}" for p in persons]


@pytest.mark.parametrize(argnames='person',
                         argvalues=persons,
                         ids=person_ids)
def test_person(person):
    assert assert_help(person)


# 参数化测试类
@pytest.mark.parametrize(argnames='person',
                         argvalues=persons,
                         ids=person_ids)
class TestPerson():
    def test_age(self, person):
        assert 18 <= person.age <= 25

    def test_height(self, person): # 这里有个缺陷，在测试类的第二个方法之后，控制台输出的测试用例名字中文会乱码
        assert 165 <= person.height <= 175

    def test_weight(self, person):
        assert 45 <= person.weight <= 60
