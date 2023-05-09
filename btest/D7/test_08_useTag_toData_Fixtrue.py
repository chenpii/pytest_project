""":使用标记的函数把数据传递给夹具
"""

import pytest


@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    if marker is None:
        # 如果maker没有匹配行，则数据为0..
        data = None
    else:
        # 否则匹配到对应的标签，着获取标记中的数据
        data = marker.args[0]

    # 对数据做一些事情
    return data


number = 42
@pytest.mark.fixt_data(number)
def test_fixt(fixt):
    assert fixt == 42
