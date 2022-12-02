import pytest
import allure
from config import *
from pages.base_page import *


@allure.feature('Test SwaggerUI')
@allure.story('STORE GET methods')
@allure.title('Test status code all get methods is 200')
@allure.step('Checking that status code all get methods is 200')
@pytest.mark.test_positive_status_code_store
@pytest.mark.parametrize('endpoint', [STORE_GET_INVENTORY])
def test_positive_status_code_store(logger, endpoint):
    should_be_page_is_found(logger, endpoint)


@allure.feature('Test SwaggerUI')
@allure.story('STORE GET methods')
@allure.title('Test content-type')
@allure.step('Checking that content-type all get methods is JSON')
@pytest.mark.test_content_type_stor
@pytest.mark.parametrize('endpoint', [STORE_GET_INVENTORY])
def test_content_type_store(logger, endpoint):
    should_be_response_json(logger, endpoint)
