"""
使用夹具提供的数据
"""

# 夹具名称直接以参数形式传入
from pytest_assume.plugin import assume


def test_some(some_data):
    assert some_data == 66


def test_student(student_score, student_name):
    with assume:  # 实际的数据长度是否跟预期长度相同
        assert len(student_score) == 2, f"实际长度{len(student_score)} 与预期长度 {2} 不相等！"

    with assume:  # 预期数据是否在实际数据内
        assert '小乐' in student_name, f"预期数据 {'小乐'} 不在实际数据{student_name}中"
