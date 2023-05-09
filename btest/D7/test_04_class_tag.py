import pytest


# 您可以使用pytest.mark带有类的装饰器将标记应用于其所有测试方法：
@pytest.mark.Wechat
class TestWechat:
    def test_talk(self):  # 聊天功能
        assert 1

    def test_friendCircle(self):  # 朋友圈
        assert 1

    def test_snake(self):  # 摇一摇
        assert 1


@pytest.mark.Meituan
class TestMeituan:
    def test_takeout(self):  # 美团外卖
        assert 1

    def test_shopGrocery(self):  # 美团买菜
        assert 1

    def test_takeTaxi(self):  # 美团打车
        assert 1

# # 对模块单个标记
# pytestmark = pytest.mark.webtest
#
# # 对模块多个名称标记
# pytestmark = [pytest.mark.webtest, pytest.mark.slowtest]
#
#
#
# # content of test_mark_classlevel.py
# import pytest
#
# # 类级别标记
# @pytest.mark.webtest
# class TestClass:
#     def test_startup(self):
#         pass
#
#     def test_startup_and_more(self):
#         pass
#
# # 这相当于直接将装饰器应用于两个测试函数。
#
# 模块级别应用标记，请使用pytestmark全局变量：
