import pytest
import allure
from config import *
from pages.user.get_page import *


@allure.feature('Test SwaggerUI')
@allure.story('USER GET methods')
@allure.title('Test login user')
@allure.step('Checking that user is login')
@pytest.mark.test_login_user
def test_login_user(logger):
    should_be_user_login(logger, USER_GET_LOGIN)


@allure.feature('Test SwaggerUI')
@allure.story('USER GET methods')
@allure.title('Test logout user')
@allure.step('Checking that user is logout')
@pytest.mark.test_logout_user
def test_logout_user(logger):
    should_be_user_logout(logger, USER_GET_LOGOUT)



