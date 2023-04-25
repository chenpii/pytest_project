'''登录案例'''

# 模拟一个登录接口
import pytest


def login(username, password):
    if (username == 'ztloo' and password == '888'):
        return '登录成功'
    else:
        return '密码错误'


# 参数化数据（官方建议形式）
user_expected = [
    ('ztloo', '888', '登录成功'),
    ('ztloo', '886', '密码错误')
]


# 适合无依赖数据，单接口测试
@pytest.mark.parametrize('username,password,expected', user_expected, ids=[1, 2])
def test_login(username, password, expected):
    assert login(username, password) == expected


#######################################################################################

user_expected_dict = [
    {
        'username': 'ztloo',
        'password': '888',
        'expected': '登录成功'
    },
    {
        'username': 'ztloo',
        'password': '886',
        'expected': '密码错误'
    }
]

user_ids = [user['expected'] for user in user_expected_dict]


@pytest.mark.parametrize(argnames='user', argvalues=user_expected_dict, ids=user_ids)
def test_login_dict(user):
    assert login(user['username'], user['password']) == user['expected']
