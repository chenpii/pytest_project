# 这是通过用例
def test_pass():
    # 期望值
    expected = 1
    # 实际值
    actual = 1
    # 通过实际值跟预期值进行相等比较，相等通过，不相等报错
    assert actual == expected


# 失败用例
def test_fail():
    # 期望值
    expected = 1
    # 实际值
    actual = 2
    # 通过实际值跟预期值进行相等比较，相等通过，不相等报错
    assert actual == expected