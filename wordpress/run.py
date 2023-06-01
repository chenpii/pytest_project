'''运行和扩展其他功能
可以同时运行UI和接口用例
也可以指定运行UI和接口

整个项目统一运行路径，包括运行接口和UI自动化用例。以及扩展其他功能。
'''
import pytest

from wordpress.config import config_map


def run(auto_type=None):
    config = config_map.get(auto_type)
    pytest.main(config.args_list)


if __name__ == '__main__':
    run(auto_type='接口')
