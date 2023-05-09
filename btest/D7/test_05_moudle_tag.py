import pytest

# 整个模块都标记为 TikTok 标签。
pytestmark = pytest.mark.TikTok


def test_tikTok_postVideo():  # 抖音发视频
    assert 1


def test_tikTok_browseVideo():  # 抖音浏览视频
    assert 1


def test_tikTok_follow():  # 抖音关注
    assert 1


def test_tikTok_clickLike():  # 抖音点赞
    assert 1
