import pytest

# 整个模块标记为 Bili 和 Soul 复合标签。
pytestmark = [pytest.mark.Bili, pytest.mark.Soul]


def test_bili_Barrage():  # 哔哩弹幕
    assert 1


def test_soul_match():  # 灵魂匹配
    assert 1
