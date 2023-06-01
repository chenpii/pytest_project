import json
import os
from urllib.parse import urljoin

import pytest
import requests

# token 全局共享，所以设置为sessio级别。
from jsonpath import jsonpath

from wordpress.config import PATH


@pytest.fixture(scope='session')
def token():
    url = 'http://www.ztloo.com/wp-json/jwt-auth/v1/token'
    payload = json.dumps({
        "username": "testBoy",
        "password": "ityige666"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    # return 'Bearer' + response.json()['token'] # token接口调不通且后续接口不用token也能正常测试
    return '123456'


@pytest.fixture
def headers(token):
    """很多用例的部分Header信息一致，封装到夹具中，减少重复。"""
    headers = {'Authorization': token,
               'Content-Type': 'application/json'
               }
    return headers


@pytest.fixture
def categories(base_url, headers, variables):
    """categories夹具。为test_categories用例提供分类数据以及数据存储到variables字典，为后续的用例做参数关联。"""
    response = requests.request('GET',
                                urljoin(base_url, 'categories'),
                                headers=headers)

    categories = response.json()
    id_ = jsonpath(categories, '$.*.id')
    name = jsonpath(categories, '$.*.name')
    id_name = dict(zip(name, id_))
    variables['categories'] = id_name  # 做全局变量关联

    return response


@pytest.fixture()
def tags(base_url, headers, variables):
    """tag标签夹具。为test_tags用例提供标签数据以及结果数据存储到variables字典，为后续的用例做参数关联。"""
    payload = {
        'per_page': 34
    }
    response = requests.request("GET",
                                urljoin(base_url, "tags"),
                                params=payload,
                                headers=headers)
    tags = response.json()
    id_ = jsonpath(tags, '$.*.id')
    name = jsonpath(tags, '$.*.name')
    id_name = dict(zip(name, id_))
    variables['tags'] = id_name

    return response


@pytest.fixture()
def upload_media(base_url, headers, variables):
    """upload_media 夹具。为test_upload_media用例提供媒体图片数据."""
    filename = 'image.jpg'
    # 用例目录
    file_path = os.path.join(PATH('api/cases/data/'), filename)
    headers.update(
        {
            'Content-Type': 'image/png',
            'Content-Disposition': 'attachment; filename=' + filename
        }
    )
    with open(file_path, 'rb') as f:
        image_data = f.read()

    response = requests.request('POST', urljoin(base_url, 'media'), headers=headers, data=image_data)
    return response
