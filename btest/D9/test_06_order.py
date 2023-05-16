'''
1、安装
pip install pytest-order -i https://pypi.douban.com/simple

2、使用序号排序，范围是全局
@pytest.mark.order(1) # 跟列表排序的规则一样。支持负数，

3、相对于其他用例排序
@pytest.mark.order(after="test_second") # 在test_second 之后运行
@pytest.mark.order(before="test_second") # 在test_second 之前运行
@pytest.mark.order(after="TestB::test_c") # 在TestB类test_c用例后运行
#在某个模块的TestA类下的test_a用例后面执行。
@pytest.mark.order(after="test_module_a.py::TestA::test_a")


4、先按照模块正常排序，然后在按模块内部序号排序
pytest tests -vv --order-scope=module


https://pytest-dev.github.io/pytest-order/stable/
'''
import pytest


@pytest.mark.order(-2)
def test_three():
    assert 1


@pytest.mark.order(index=-1)  # 第四个
def test_four():
    assert 1


@pytest.mark.order(index=2)
def test_two():
    assert 1


@pytest.mark.order(1)
def test_one():
    assert 1
