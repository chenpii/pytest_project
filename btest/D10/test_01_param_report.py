import pytest


def login(username, password):
    if username == 'ztloo' and password == '888':
        return '登陆成功'
    else:
        return '密码错误或账号不存在'


user_expected = [
    pytest.param('ztloo', '888', '登陆成功',
                 marks=pytest.mark.dependency(name="user_1")),
    pytest.param('admin', '888', '登陆成功',
                 marks=pytest.mark.dependency(name="user_2"))
]


@pytest.mark.parametrize('username,password,expected', user_expected)
def test_login(username, password, expected):
    assert login(username, password) == expected


show_expected = [
    pytest.param('ztloo', '首页包含ztloo用户名',
                 marks=pytest.mark.dependency(name="show_1", depends=["user_1"])),
    pytest.param('admin', '首页包含admin用户名',
                 marks=pytest.mark.dependency(name="show_2", depends=["user_2"]))
]


@pytest.mark.parametrize('username,expected', show_expected)
def test_show_index(username, expected):
    assert username in expected
