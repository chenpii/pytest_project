'''
夹具形式提供数据

# 1、安装
pip install pytest-variables[yaml]

# 2、准备用例需要的数据。
[pytest]
addopts =
    --variables ./data/my_api.json
    --variables ./data/user.yml

# 3、my_api.json
{
  "foo": "bar",
  "bar": "foo"
}

user.yml
test_login: # 用例名称
  # 用户名,密码,期望结果,
  username: "testBoy"
  password: "123456"
  expected: "仪表盘"


test_logout:
  username: "testGirl"
  password: '123456'
  expected: "欢迎再来"

# 4、使用数据
'''


def test_json(variables):
    assert variables['foo'] == 'bar'

def test_login(case_data):
    assert case_data['expected'] == '仪表盘'

def test_logout(case_data):
    assert case_data['expected'] == '欢迎再来'

