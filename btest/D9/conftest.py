import pytest


@pytest.fixture
def case_data(request, variables):
    testcase_name = request.function.__name__
    return variables[testcase_name]
