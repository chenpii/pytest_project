'''自定义异常信息'''
import pytest
from pytest_assume.plugin import assume

from btest.D1 import student


def test_student_name_hard_custom_fail():
    actual = student.student_name()
    with assume:  # 实际的数据长度是否跟预期长度相同
        assert len(actual) == 3, \
            f"实际数据长度:{len(actual)} 与预期数据长度:{3} 不相同！"

    with assume:  # 预期数据是否在实际数据内
        assert '小红1' in actual, \
            f"预期数据: {'小红1'} 没在 实际数据中:{actual}！"

    if ('小乐' not in actual):  # 不推荐
        pytest.fail(f"预期数据：小乐，没有在实际数据中！")
