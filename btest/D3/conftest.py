"""
共享夹具
提供测试数据
"""
import pytest


@pytest.fixture
def some_data():
    print("生成 some_data")
    return 66


@pytest.fixture
def student_score():
    print("生成 student_score")
    return {'小明': 99, '小红': 100}


@pytest.fixture
def student_name():
    print("生成 student_name")
    return ['小明', '小红']


@pytest.fixture
def mail_admin():
    from btest.D3.mail import MailAdminClient
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    print('\n--sending_user创建发送用户-------\n')

    yield user

    print('\n--sending_user删除发送用户-------\n')
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    print('\n--sending_user创建接收用户-------\n')

    yield user

    print('\n--sending_user删除接收用户-------\n')
    mail_admin.delete_user(user)
