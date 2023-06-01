import pytest
from jsonpath import jsonpath
from pytest_assume.plugin import assume
import logging

# 接口自动化测试用例:

##############################################################
# step 1: 获取token (前置 : token)

# step 2: 获取分类  （case-1：test_categories）
# step 3: 获取标签   （case-2: test_tags）
# step 4: 创建图片媒体、返回媒体id (case-3:test_upload_media)
# step 5: 发布文章,关联(分类、标签、以及媒体id图片) (case-4:test_post_article)

# step 6、删除文章和图片 (后置-清理:)  del_article


##############################################################


LOGGER = logging.getLogger(__name__)  # 模块级记录器


@pytest.mark.parametrize('stat_code,excepted', [(200, 'python')])
def test_categories(categories, variables,
                    stat_code, excepted):
    """
    :param categories:以plugins文件夹中my_api插件提供分类数据
    :param variables:为整个测试的全局字典。存储用例数据、和用例关联的参数
    :param stat_code:用例预测状态码：200
    :param excepted:用例结果期望值：python
    :return:
    """

    with assume:
        assert categories.status_code == stat_code

    with assume:
        assert excepted in variables['categories']

    LOGGER.info(f'test_categories-{categories.status_code}')


@pytest.mark.parametrize('stat_code,excepted', [(200, 'python')])
def test_tags(tags, variables, stat_code, excepted):
    """
    :param tags: 以plugins文件夹中my_api插件提供分类数据
    :param variables: 为整个测试的全局字典。存储用例数据、和用例关联的参数
    :param stat_code: 用例预测状态码：200
    :param excepted: 用例结果期望值：python
    :return:
    """
    with assume:
        assert tags.status_code == stat_code
    with assume:
        assert excepted in variables['tags']

    LOGGER.info(f'test_tags-{tags.status_code}')


@pytest.mark.parametrize('stat_code', [200])
def test_media(upload_media, variables, stat_code):
    """
    验证状态码是否为201和media_id 存储到variables全局字典中，并把测试用例名字和图片id记录在日志文件中。
    :param uploda_media:以plugins文件夹中my_api插件提供上传图片功能。
    :param variables:为整个测试的全局字典。存储用例数据、和用例关联的参数
    :param stat_code: 状态码成功：201
    :return:
    """
    with assume:
        assert upload_media.status_code == stat_code

    variables['media_id'] = jsonpath(upload_media.json(), '$.*.id')  # 把图片id,存储到全局字典。

    LOGGER.info(f"test_upload_media-{variables['media_id']}")
