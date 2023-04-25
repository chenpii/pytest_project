# 解决中文乱码
# pytest中的钩子函数，用于收集测试用例，且在测试用例收集完毕之后被调用
# items：用例对象,可以通过它改变用例顺序和显示等。

# pytest 会提供一些钩子函数，来满足我们一些需求。
def pytest_collection_modifyitems(items):
    print(items)
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print('item.name:', item.name)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        print('item._nodeid:', item._nodeid)
