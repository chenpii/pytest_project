import time

import pytest

"""
1、安装pip install pytest-timeout -i https://pypi.douban.com/simple


2、全局超时
[pytest]
timeout = 300

3、环境变量（PYTEST_TIMEOUT）设置全局超时，覆盖配置文件

4、--timeout命令行选项设置覆盖环境变量和配置选项的全局超时
pytest --timeout=300

5、单个用例超时
@pytest.mark.timeout(6)

https://github.com/pytest-dev/pytest-timeout
"""


@pytest.mark.timeout(2)  # 设置单个用例超时
def test_add():
    time.sleep(4)
    assert 1


def test_update():
    assert 1