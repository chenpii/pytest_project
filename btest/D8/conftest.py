import pytest

from btest.D2.face_to_object import Person

'''
完善做饭接口
'''


@pytest.fixture(autouse=True)
def cook(mocker):  # 提供模拟Person中cook做饭接口数据
    food = {'result': '酸辣土豆丝'}
    return mocker.patch.object(Person, 'cook', return_value=food)


def mock_func(food):  # 模拟函数功能
    if food == '虾仁西蓝花':
        return {'status': '还可以'}
    elif food == '酸辣土豆丝':
        return {'status': '还不错'}
    elif food == '西红柿炒鸡蛋':
        return {'status': '太好吃'}
    else:
        return {'result': '产生异常', 'status': 500}


@pytest.fixture(autouse=True)  # 提供模拟Person中eat吃饭接口数据
def eat(mocker):
    return mocker.patch.object(Person, 'eat', side_effect=mock_func)
