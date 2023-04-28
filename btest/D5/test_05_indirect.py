'''
间接参数化
官方对indirect解释：

在参数化测试时，使用参数允许在将值传递给测试之前, 使用夹具接收值来参数化测试：indirect=True

如果为 True，则列表包含 argnames 中的所有名称。与此列表中的 argname 对应的每个 argvalue 将作为 request.param 传递给其各自的 argname 夹具函数


（说明：如果有夹具名为user，会把[“管理员”, “会员”, “游客”] 传给 名为user的fixture夹具。
在user夹具内部，使用request.param来接收传过来的参数数据，得到数据你可以选择二次加功能。
加工过的数据，自动的返回给我们的用例。
作用：在不改变参数列表和用例内部逻辑的情况下，间接的对参数进行了处理。
'''
import pytest


@pytest.fixture()
def user(request):  # user是夹具
    function_name = request.function.__name__
    # 这里不使用request.param的原因是有时候没有参数会报错，所以使用getattr(request,'param','游客')来对没参数时进行一个默认赋值
    # role = request.param
    role = getattr(request, 'param', '游客')  # 当没有参数时，返回游客

    print(f'\n-----{function_name}:登陆角色为:{role}----')
    yield f'我是{role}'
    print(f'----{function_name}:登出角色为:{role}----\n')


@pytest.mark.parametrize(argnames='user',
                         argvalues=['管理员', '会员', '游客'],
                         indirect=True  # 开启，则会寻找跟参数名一样的夹具，找到后把参数传递给夹具
                         )
def test_acess(user):
    print(f'访问权限测试 {user}')


def test_user(user):  # 未指定用户
    print(f"访问权限测试 {user}")  # 访问权限测试 俺是游客


#################################################################################

@pytest.fixture()
def method_indirect(request):
    # 可以通过request.param接受传递过来的参数，二次处理
    return '我是夹具' + request.param


@pytest.fixture()
def x(request):
    return '我是x夹具' + request.param


# 个人理解：如果indirect为True，那么会将参数值先传递给跟参数名相同的夹具，夹具可能对参数做了处理之后再返回给测试用例
@pytest.mark.parametrize(argnames='method_indirect,x',
                         argvalues=[('method_A', '1'), ('method_B', '2'), ('method_C', '3')],
                         indirect=True)
def test_indirect(method_indirect, x):
    print(f'我是变量  {method_indirect}')
    print(f'我是变量  {x}')
