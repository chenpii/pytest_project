import pytest


@pytest.fixture(scope='module')
def make_customer_record():
    created_records = []

    # 隐藏式函数，增强函数内部功能。生成数据的过程放在函数里
    # （不建议。让夹具的代码变得非常臃肿，可读性非常低。最好把夹具拆开，以互相引用的方式）
    def _make_customer_record(name):
        records = {"name": name}
        created_records.append(records)
        return created_records

    yield _make_customer_record

    for record in created_records:
        record.clear()


def test_customer_records_1(make_customer_record):
    make_customer_record("小明")


def test_customer_records_2(make_customer_record):
    make_customer_record("小乐")


def test_customer_records_3(make_customer_record):
    data = make_customer_record("小红")
    assert data == [{'name': '小明'}, {'name': '小乐'}, {'name': '小红'}]
