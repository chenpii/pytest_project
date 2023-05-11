'''
替换内置模块功能
'''
import os

from pytest_assume.plugin import assume


class FileSystem:
    @staticmethod
    def lsd():
        return os.listdir()


# mocker 是pytest-mock提供的模拟夹具
def test_unix_fs(mocker):
    mocker.patch('os.listdir', return_value=['1', '2'])
    with assume:
        assert os.listdir() == ['1', '2']

    with assume:
        assert FileSystem.lsd() == ['1', '2']


'''
pytest.ini里面加上
[pytest]
disable_test_id_escaping_and_forfeit_all_rights_to_community_support = True
用于支持中文

'''
