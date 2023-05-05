p = 'lyf'


def test_tmp_factory_1(tmp_factory):
    with open(tmp_factory, mode='a+') as f:
        f.write(p)
    assert tmp_factory.read_text() == 'hellolyf'


def test_tmp_factory_2(tmp_factory):
    with open(tmp_factory, mode='a+') as f:
        f.write('beautiful')
    assert tmp_factory.read_text() == 'hellolyfbeautiful'
