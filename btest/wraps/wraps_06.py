"""
在类的方法上使用装饰器

"""
import time
from functools import wraps

# 自定义重复请求的次数，和间隔的秒数
import requests


def retry_request(retries=3, delay=5):
    def try_request(func):
        @wraps(func)
        def retry_decorators(*args, **kwargs):
            for i in range(retries):
                res = func(*args, **kwargs)
                print(res)
                time.sleep(delay)

        return retry_decorators

    return try_request


class ApiRequest:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    @retry_request(retries=3, delay=5)
    def create_reques(self):
        res = requests.get(self.url, self.headers)
        return res


aq = ApiRequest('http://www.baidu.com', headers=None)
aq.create_reques()
