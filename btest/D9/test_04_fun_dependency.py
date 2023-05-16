'''
# 1、安装
pip install pytest-dependency -i https://pypi.douban.com/simple

# 2、参考文档
https://pytest-dependency.readthedocs.io/en/stable/usage.html
'''
import pytest


@pytest.mark.dependency(name='a')
def test_a():
    assert False


# 我依赖test_a，只有a用例通过，b用例才会执行
@pytest.mark.dependency(depends=['a'])
def test_b():
    assert True


class TestClassNamed:
    @pytest.mark.dependency(name='c')
    def test_c(self):
        assert True

    # 我是用例d,我依赖c 用例。
    @pytest.mark.dependency(name='d', depends=['c'])
    def test_d(self):
        assert True

    @pytest.mark.dependency(name='e')
    def test_e(self):
        assert True

    # 我是用例f ,我依赖d和e用例。只有d和e用例都通过，我才执行。
    @pytest.mark.dependency(depends=['d', 'e'])
    def test_f(self):
        assert True
