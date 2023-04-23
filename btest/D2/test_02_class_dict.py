from btest.D2.face_to_object import Person


# 期望值是一个对象，但是接口返回是一个字典，需要将字典转换成数据对象
def test_from_dict():
    # 期望的对象
    expected_p = Person("lyf", 18, 170, 60)

    # 实际返回字典
    actual_p_dict = {
        "name": "lyf",
        "age": 18,
        "height": 170,
        "weight": 60
    }

    # 实际的对象
    actual_p = Person.from_dict(actual_p_dict)
    assert actual_p == expected_p


# 期望值是字典，但是接口返回数据对象，需要将对象转换成字典
def test_to_dict():
    # 期望字典值
    expected_p_dict = {
        "name": "lyf",
        "age": 21,
        "height": 170,
        "weight": 60
    }

    # 实际对象
    actual_p = Person("lyf", 18, 170, 60)

    # 实际字典值
    actual_p_dict = actual_p.to_dict()
    assert expected_p_dict == actual_p_dict
