import pytest


@pytest.fixture(scope='session', autouse=True)
def student_score():
    print("\n>>>>>>>>>>>>>>>>>session: 测试开始-环境初始化>>>>>>>>>>>>>>>>>>>>>>>>>")
    yield
    print("\n>>>>>>>>>>>>>>>>>session: 测试完成-环境清理>>>>>>>>>>>>>>>>>>>>>>>>>")


@pytest.fixture(scope='module', autouse=True)
def login_logout(request):
    modle_name = request.module.__name__
    print(f"\n------------------{modle_name}:登录成功------------------")
    yield
    print(f"\n------------------{modle_name}:注销登录------------------")


@pytest.fixture()
def input_info(request):
    function_name = request.function.__name__
    print(f"\n***{function_name}:开始输入信息***")
    yield
    print(f"\n***{function_name}:结束输入信息***")


@pytest.fixture(scope='class')
def student(request):
    class_name = request.cls.__name__
    print(f'+++class:{class_name}:输入学生信息+++')
    student_info = {
        '小明': 90,
        '小红': 100
    }
    yield student_info
    student_info.clear()
    print(f'+++class:{class_name}:清空学生信息+++')
