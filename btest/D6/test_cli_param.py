# 把多个命令行选项参数化测试

# pytest -qs --stringinput=abc --stringinput=123 ./test_cli_param.py
def test_valid_string(stringinput):
    print(stringinput)
    assert stringinput.isalpha()
