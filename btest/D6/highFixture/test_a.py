def test_dynamic(student):
    student.append('小明')
    assert student == ['小明']


# scope 为模块级别通过。 pytest -sv --scope=module .\test_a.py
def test_dynamic_moudle(student):
    student.append('小红')
    assert student == ['小明', '小红']
