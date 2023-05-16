'''
1、安装
pip install pytest-rerunfailures  -i https://pypi.douban.com/simple

2、把失败的重新运行5次
pytest --reruns 5

3、重新下一次运行进行延迟等待 1秒
pytest --reruns 5 --reruns-delay 1

4、只会重新运行某种异常的用例
pytest --only-rerun AssertionError

5、运行AssertionError 或ValueError 的用例
pytest --reruns 5 --only-rerun AssertionError --only-rerun ValueError

6、只会重新运行匹配 某某Error 以外的错误：
pytest --reruns 5 --rerun-except AssertionError
pytest --reruns 5 --rerun-except AssertionError --rerun-except OSError

7、标记某个用例，失败时最多重复5次
@pytest.mark.flaky(reruns=5)

8、标记某个用例，失败时最多重复5次，每次的延时时间
@pytest.mark.flaky(reruns=5, reruns_delay=2)

9、您还可以在重新运行标记中指定可选条件：
@pytest.mark.flaky(reruns=5, condition=sys.platform.startswith("win32"))

'''
import pytest


@pytest.mark.flaky(reruns=5)
def test_error_1():
    assert 0


def test_error_2():
    assert 0


def test_pass():
    assert 1
