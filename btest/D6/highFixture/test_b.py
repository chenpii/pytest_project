def test_dynamic_b1(student):
    student.append('小亮')


# scope 为session级别通过。
def test_dynamic_b2(student):
    student.append('小乐')
    assert student == ['小明', '小红', '小亮', '小乐']
