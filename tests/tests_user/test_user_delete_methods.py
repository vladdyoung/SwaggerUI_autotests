import pytest
import allure
from config import *
from pages.user.delete_page import *
from pages.user.post_page import *


@allure.feature('Test SwaggerUI')
@allure.story('User DELETE method')
@allure.title('Test delete user')
@allure.step('Checking that user is delete')
@pytest.mark.test_delete_user
def test_delete_user(logger):
    create_user(logger, USER_POST_CREATE_USER)
    should_be_create_user(logger, USER_POST_CREATE_USER)
    delete_user(logger, USER_POST_CREATE_USER)
    should_be_delete_user(logger, USER_POST_CREATE_USER)
