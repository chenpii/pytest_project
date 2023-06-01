'''全局配置模块，为经常需要修改的配置项
如常量、路径、邮箱账号密码、配置属性信息等
'''
import os


def PATH(p=''):
    # 传进相对路径，返回绝对路径
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class Config(object):
    """配置信息"""
    # 对于项目路径规划, 路径分隔符号一律左撇/，win与linux 同步防止转义
    PROJECT = '接口测试'
    TESTER = 'TEST'  # 测试人员
    QQ = '123456789'  # 联系方式


class InterfaceConfig(Config):
    """接口自动化测试环境信息"""
    REPORT_TITLE = Config.PROJECT + '接口自动化'  # 测试标题
    env_name = '生产环境'

    # 用例目录
    CASE_PATH = PATH('api/cases/')
    CASE_DATA_PATH = CASE_PATH + '/data/'

    # pytest.main用例执行参数列表
    args_list = [CASE_PATH]


class UIConfig(Config):
    pass


# 后续环境配置复杂了，再开启
config_map = {
    "接口": InterfaceConfig,
    "UI": UIConfig,
}

if __name__ == '__main__':
    print(config_map.get('接口').CASE_PATH)
