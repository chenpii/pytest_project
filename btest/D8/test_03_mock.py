'''
字典替换功能
'''
from pytest_assume.plugin import assume


def test_mock_dict(mocker):
    student_score = {"小红": 99}
    mocker.patch.dict(student_score, values=[("小明", 100)], clear=True)  # 清除老字典，替换新字典
    with assume:
        assert student_score == {"小明": 100}

    mocker.resetall()  # 重置所有活动补丁
    with assume:
        assert student_score == {'小明': 100}

    mocker.stopall()  # 停止所有活动补丁
    with assume:
        assert student_score == {"小红": 99}