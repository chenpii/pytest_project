'''
参数生成器

param 函数：在pytest.mark.parametrize 参数装饰器中可以作为一个指定的参数进行调用



'''

import pytest

from btest.D1.student import student_score


# 可以指定参数
def student_score_params():
    for key, value in student_score().items():
        yield pytest.param(value, id=key)


@pytest.mark.parametrize('score', student_score_params())
def test_student_score(score):
    assert score > 90


