import pytest
import allure
from config import *
from pages.user.post_page import *


@allure.feature('Test SwaggerUI')
@allure.story('USER POST methods')
@allure.title('Test create user')
@allure.step('Checking that user was created')
@pytest.mark.test_create_user
def test_create_user(logger):
    create_user(logger, USER_POST_CREATE_USER)
    should_be_create_user(logger, USER_POST_CREATE_USER)


@allure.feature('Test SwaggerUI')
@allure.story('USER POST methods')
@allure.title('Test create user with array')
@allure.step('Checking that user with array was created')
@pytest.mark.test_create_user_with_array
def test_create_user_with_array(logger):
    should_be_create_user_with(logger, USER_POST_CREATE_USER_WITH_ARRAY)


@allure.feature('Test SwaggerUI')
@allure.story('USER POST methods')
@allure.title('Test create user with list')
@allure.step('Checking that user with list was created')
@pytest.mark.test_create_user_with_list
def test_create_user_with_list(logger):
    should_be_create_user_with(logger, USER_POST_CREATE_USER_WITH_LIST)
