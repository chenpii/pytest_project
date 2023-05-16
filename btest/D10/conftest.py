import pytest
from py.xml import html


# 修改报告标题
def pytest_html_report_title(report):
    report.title = "同乐学堂自动化测试报告"


# 在运行测试之前修改Environment（运行环境）
def pytest_configure(config):
    # 环境字典 使用pop删除，即使没有对应的数据，也会返回默认值1
    config._metadata.pop('JAVA_HOME', 1)
    config._metadata.pop('Packages', 1)
    config._metadata.pop('Plugins', 1)


# 运行之后修改Environment
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["被测系统"] = "同乐学堂"


# 使用钩子编辑Summary（总结）
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("所属部门: 质量部门")])
    prefix.extend([html.p("测试人员: 小乐")])
    prefix.extend([html.p("联系QQ: 1071235258")])


# 表格header修改，把初始化得4列进行替换
def pytest_html_results_table_header(cells):
    cells[0] = html.th("用例执行结果", class_="sortable result initial-sort", col="result")
    cells[1] = html.th("时间", class_="sortable time", col="time")
    cells[2] = html.th("测试用例", class_="sortable", col="name")
    cells[3] = html.th("持续时间", class_="sortable", col="duration")


# 表格单元格修改
def pytest_html_results_table_row(report, cells):
    from datetime import datetime
    dt = datetime.now()
    cells.insert(1, html.td(dt.strftime('%Y-%m-%d %H:%M:%S'), class_="col-time"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
