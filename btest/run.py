"""
# 终端控制台命令
# 1. pytest
# 2. pytest -sv 详细信息
# 3. pytest -q .\D1         # 指定package
# 4. pytest -q .\D1\test_01_pass_fail.py    # 指定模块
# 5. pytest -q .\D1\test_05_exception.py::test_student_score_raise  # 指定测试用例
"""
import pytest

if __name__ == '__main__':
    '''D1'''
    # 运行当前目录所有用例，并展示详细信息
    pytest.main(['-sv'])
    # 运行指定目录下的所有用例，并展示简要结果信息
    # pytest.main(['-q', '.\\D1'])
