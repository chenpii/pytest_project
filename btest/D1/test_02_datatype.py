from btest.D1 import student


# 这是student_score 验证全数据等式用例
def test_student_score():
    # 期望值
    expected = {'小明': 99, '小红': 100}
    # 实际值
    actual = student.student_score()
    # 通过实际值跟预期值进行相等比较，相等通过，不相等报错
    assert actual == expected


# student_score 验证部分数据等式用例
# 验证小红成绩是否等于100 是：pass 否：fail
def test_student_score_other():
    # 期望值
    expected = 100
    # 实际值
    actual = student.student_score()['小红']
    # 通过实际值跟预期值进行相等比较，相等通过，不相等报错
    assert actual == expected


# 这是student_name 的包含用例
# 验证小明是否在学生姓名列表中，是：pass，否：fail
def test_student_name():
    # 期望值
    expected = '小明'
    # 实际值
    actual = student.student_name()
    # 通过预期值是否在实际值中，在：pass，不在：fail
    assert expected in actual
