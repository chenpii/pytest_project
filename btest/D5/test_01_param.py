import pytest


# 方式1： 普通自定义参数化。优点：可控性强。
@pytest.fixture
def input_expecteds():  # 实际输入数据："3+5"和 预期结果：8
    yield [("3+5", 8), ("2+4", 66), ("6*9", 42)]


def test_eval_sample(input_expecteds):
    from pytest_assume.plugin import assume

    for data in input_expecteds:
        act_input, expected = data[0], data[1]
        with assume:
            assert eval(act_input) == expected


# 方式2: 参数化夹具。优点：可以共享
@pytest.fixture(params=[("3+5", 8), ("2+4", 66), ("6*9", 42)], ids=[1, 2, 3])
def actual_input_expected(request):
    yield request.param


def test_eval_fixture_param(actual_input_expected):
    print(actual_input_expected)
    act_input, expected = actual_input_expected
    assert eval(act_input) == expected


# 方式3：参数化装饰器。优点：简洁、可读性强
@pytest.mark.parametrize(argnames="actual_input,expected,abc",
                         argvalues=[("3+5", 8, 9), ("2+4", 66, 1), ("6*9", 42, 2)],
                         indirect=False,
                         ids=[1, 2, 3])
def test_eval(actual_input, expected, abc):
    assert eval(actual_input) == expected
