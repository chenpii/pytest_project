import pytest

# 整个模块都标记为 Baidu 标签。
pytestmark = pytest.mark.Baidu


def test_baidu_search():  # 百度搜索
    assert 1


def test_baidu_setting():  # 百度设置
    assert 1


def test_baidu_knows():  # 百度知道
    assert 1

