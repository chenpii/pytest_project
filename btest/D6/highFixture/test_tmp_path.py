name = 'lyf'


def test_tmp_1(tmp_file):
    with open(tmp_file, mode='a+') as f:
        f.write(name)

    assert tmp_file.read_text() == 'hellolyf'


def test_tmp_2(tmp_file):
    with open(tmp_file, mode='a+') as f:
        f.write('beautiful')
    assert tmp_file.read_text() == 'hellolyfbeautiful'
