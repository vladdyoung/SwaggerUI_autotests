import pytest
import allure
from config import *
from pages.user.put_page import *
from pages.user.post_page import *


@allure.feature('Test SwaggerUI')
@allure.story('User PUT method')
@allure.title('Test update user')
@allure.step('Checking that user is update')
@pytest.mark.test_put_user
def test_put_user(logger):
    create_user(logger, USER_POST_CREATE_USER)
    should_be_create_user(logger, USER_POST_CREATE_USER)
    put_user(logger, USER_PUT)
    should_be_put_user(logger, USER_POST_CREATE_USER)
