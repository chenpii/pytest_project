#  pytest -sq --cmdopt=type2 .\test_cli_cmdopt.py
def test_answer(cmdopt):
    if cmdopt == 'type1':
        print('first')
    elif cmdopt == 'type2':
        print('seconc')
    assert 1
