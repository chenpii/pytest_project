'''异常捕获'''
import pytest

from btest.D1.student import student_score


# 通过try/finally 处理用例异常
def test_student_score_error():
    actual = student_score()
    try:
        actual['小红'] = actual['小红'] + '10'  # 代码异常
    except:
        pass
    finally:
        assert '小乐' in actual, "小乐没有在学生成绩表中！"


# pytest用例异常处理
def test_student_score_raise():
    actual = student_score()
    with pytest.raises(Exception):  # 更具可读性且不易出错。
        actual['小红'] = actual['小红'] + '10'
        # assert '小乐' in actual , "小乐没有在学生成绩表中！"# 不会执行

    # 会执行
    assert '小乐' in actual, "小乐没有在学生成绩表中！"
