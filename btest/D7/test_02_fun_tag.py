import pytest


@pytest.mark.Wechat
def test_talk():  # 聊天功能
    assert 1


@pytest.mark.Meituan
def test_takeout():  # 美团外卖
    assert 1


@pytest.mark.Wechat
def test_friendCircle():  # 朋友圈
    assert 1


@pytest.mark.Meituan
def test_shopGrocery():  # 美团买菜
    assert 1


@pytest.mark.Meituan
def test_takeTaxi():  # 美团打车
    assert 1
