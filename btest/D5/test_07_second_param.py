"""
多个夹具的间接参数化

使用场景：组装拼接参数或把很长很多的参数拆开分为夹具进行开发
"""
import pytest
from pytest_assume.plugin import assume

from btest.D2.face_to_object import Person


@pytest.fixture(params=['lyf', 'ym'])
def person_name(request):
    '''
       生成2个结果 lyf,ym
    '''
    # return Person(request.param, 0)
    return request.param


@pytest.fixture(params=[18, 30])
def person_age(person_name, request):
    '''生成4个结果
        lyf-18
        lyf-30
        ym-18
        ym-30
    '''
    # return Person(person_name, request.param)
    return request.param


@pytest.mark.parametrize(argnames='height,weight',
                         argvalues=[(160, 65), (170, 55)])
def test_person_object(person_name, person_age, height, weight):
    # person_name 是夹具名，被测试用例调用时，是夹具的返回结果
    print(f'\nperson_name:{person_name}')
    print(f'\nperson_age:{person_age}')

    p = Person(person_name, person_age, height, weight)

    print(f'\np:{p}')
    with assume:
        assert p.height == height

    with assume:
        assert p.weight == weight


# 参数化堆叠
# 自动根据参数数据的格数自动排列组合成一组测试数据，适合多条件组合
@pytest.mark.parametrize('height,weight', [(160, 65), (170, 55)])
@pytest.mark.parametrize('name', ['dlrb', 'yz'])
@pytest.mark.parametrize('age', [25, 29])
def test_person(name, age, height, weight):
    p = Person(name, age, height, weight)
    assert p.height == height
