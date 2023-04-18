from pytest_assume.plugin import assume

# hard代表严格详细的测试
from btest.D1 import student


def test_student_score_hard():
    actual = student.student_score()
    with assume:  # 实际数据类型是否跟预期数据类型一致
        assert isinstance(actual, dict)

    with assume:  # 实际的数据长度是否跟预期长度相同
        assert len(actual) == 2

    with assume:  # 预期数据是否在实际数据内
        assert '小明' in actual

    with assume:  # 实际数据是否等于预期数据
        assert actual['小红'] == 100
