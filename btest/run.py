"""
# 终端控制台命令
# 1. pytest
# 2. pytest -sv 详细信息
# 3. pytest -q .\D1         # 指定package
# 4. pytest -q .\D1\test_01_pass_fail.py    # 指定模块
# 5. pytest -q .\D1\test_05_exception.py::test_student_score_raise  # 指定测试用例
"""
import os
import time

import pytest


# allure执行函数
def mk_allure_report():
    # 准备好报告工具、和报告的存储目录 以及web服务的IP地址和端口号
    ALLURE_PATH = os.getcwd() + "\\D10\\allure-2.18.0\\bin"
    ALLURE_RESULTS = os.getcwd() + "\\D10\\report\\allure-results"
    ALLURE_REPORT = os.getcwd() + "\\D10\\report\\allure-report"
    ALLURE_SERVER_IP = "127.0.0.1"
    ALLURE_SERVER_PORT = "8086"

    # 执行用例
    pytest.main(['-sq', '--alluredir', ALLURE_RESULTS, ".\\D10\\"])

    # 把ALLURE_RESULTS目录的结果数据-->生成报告到ALLURE_REPORT目录下
    mk_report_cmd = f"{ALLURE_PATH}/allure " \
                    f"generate " \
                    f"-c {ALLURE_RESULTS} " \
                    f"-o {ALLURE_REPORT}"
    os.popen(mk_report_cmd)

    time.sleep(3)  # 因生成报告需要时间，强制等待。

    # 打开报告web 服务
    open_report_cmd = f"{ALLURE_PATH}/allure " \
                      f"open " \
                      f"-h {ALLURE_SERVER_IP} " \
                      f"-p {ALLURE_SERVER_PORT} {ALLURE_REPORT}"
    os.popen(open_report_cmd)


if __name__ == '__main__':
    '''D1'''
    # 运行当前目录所有用例，并展示详细信息
    # pytest.main(['-sv'])
    # 运行指定目录下的所有用例，并展示简要结果信息
    # pytest.main(['-q', '.\\D1'])
    # pytest.main(['-q', '.\\D1\\test_01_pass_fail.py'])
    # pytest.main(['-q', '.\\D1\\test_05_exception.py::test_student_score_raise'])

    '''D4篇'''
    # 通过关键字表达式进行测试
    # pytest.main(['-qs', '-k', 'student', '.\\D4\\'])

    '''D5篇'''
    # pytest.main(['-qs', '.\\D5\\test_05_indirect.py'])
    # pytest.main(['-qs', '.\\D5\\test_06_subset_param.py'])
    # pytest.main(['-sv', '.\\D5\\test_07_second_param.py'])

    '''D6篇'''
    # # 自定义命令行参数
    # pytest.main(['-sv', '--scope=module', '.\\D6\\highFixture\\test_a.py'])
    # pytest.main(['-sv', '-k', 'dynamic', '--scope=session', '.\\D6\\highFixture'])
    # pytest.main(['-sv',  '.\\D6\\highFixture\\test_tmp_path_factory.py'])

    '''D7篇 运行标签'''
    # # 添加'--runslow'相当于（"--runslow=True"）带有slow标签的用例才会执行，否则跳过不执行。
    # pytest.main(['-sv', '.\\D7\\test_01_cli_skip_tag.py'])
    # pytest.main(['-sv', '--runslow', '.\\D7\\test_01_cli_skip_tag.py'])
    # # 运行标签为Wechat的所有用例
    # pytest.main(['-sv', '-m', 'Wechat', '.\\D7\\'])
    # # 运行非Wechat标签的所有用例。包括未标签的和已标签的
    # pytest.main(['-sv', '-m', 'not Wechat', '.\\D7\\'])
    # # 只运行Wechat标签和Meituan这两个标签的用例
    # pytest.main(['-sv', '-m', 'Wechat or Meituan', '.\\D7\\'])
    # # 只运行Meituan标记的类
    # pytest.main(['-sv', '-m', 'Meituan', '.\\D7\\test_04_class_tag.py'])
    # # 只运行TikTok标记的模块
    # pytest.main(['-sv', '-m', 'TikTok', '.\\D7\\'])
    # # 运行标记了Bili 和Soul的模块
    # pytest.main(['-sv', '-m', 'Bili and Soul', '.\\D7\\'])

    '''D8 mock'''
    # pytest.main(['-sv', '.\\D8\\test_02_mock.py'])
    # pytest.main(['-sv', '.\\D8\\test_03_mock.py'])

    '''D9 plugins'''
    # pytest.main(['-sv', '.\\D9\\test_02_repeat.py'])
    # pytest.main(['-sv', '.\\D9\\test_03_error_repeat.py'])
    # pytest.main(['-sv', '.\\D9\\test_04_fun_dependency.py'])
    # pytest.main(['-sv', '.\\D9\\test_05_param_dependency.py'])
    # pytest.main(['-sv', '.\\D9\\test_06_order.py'])
    # pytest.main(['-sv', '.\\D9\\test_07_base_url.py'])

    '''D10 '''
    mk_allure_report()
