'''
子集参数化

利用参数化装饰器，覆盖掉参数化夹具中的参数数据，缩小参数数据范围，从而变成子集。
'''

import pytest


# 参数化夹具
@pytest.fixture(params=['管理员', '会员', '游客'])
def user(request):
    function_name = request.function.__name__
    role_name = request.param

    print(f'\n------{function_name}登录角色为{role_name}------')
    yield role_name
    print(f'\n------{function_name}登出角色为{role_name}------')


def test_everyone(user):
    print(f'\n访问权限测试角色{user}')

# 参数化装饰器
# 当用例使用了参数化装饰器，参数化装饰器里面的参数就会覆盖掉参数化夹具中的参数
@pytest.mark.parametrize('user', ['管理员'], indirect=['user'])
def test_just_admin(user):
    print(f'\n访问权限测试角色{user}')
