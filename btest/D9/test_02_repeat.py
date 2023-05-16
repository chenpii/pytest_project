"""
1、安装
pip install pytest-repeat -i https://pypi.douban.com/simple

2、运行重复次数
 pytest --count=10 test_file.py

3、单个用例重复几次
@pytest.mark.repeat(3)

4、重复测试到失败
pytest --count=1000 -x test_file.py

https://github.com/pytest-dev/pytest-repeat
"""
import pytest


def test_hello():
    assert 1


@pytest.mark.repeat(3)  # 单个用例重复执行
def test_world():
    assert 1


def test_python():
    assert 1
