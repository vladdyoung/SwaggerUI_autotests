import pytest
import allure
from config import *
from pages.store.post_page import *


@allure.feature('Test SwaggerUI')
@allure.story('STORE POST methods')
@allure.title('Test create order')
@allure.step('Checking that order is create')
@pytest.mark.test_create_order
def test_create_order(logger):
    create_order(logger, STORE_GET_ORDER_ID)
    should_be_create_order(logger, STORE_GET_ORDER_ID)
