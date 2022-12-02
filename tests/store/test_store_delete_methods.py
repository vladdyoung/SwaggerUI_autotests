import pytest
import allure
from config import *
from pages.store.delete_page import *
from pages.store.post_page import *


@allure.feature('Test SwaggerUI')
@allure.story('STORE DELETE method')
@allure.title('Test delete order')
@allure.step('Checking that order is delete')
@pytest.mark.test_delete_order
def test_delete_order(logger):
    create_order(logger, STORE_GET_ORDER_ID)
    should_be_create_order(logger, STORE_GET_ORDER_ID)
    delete_order(logger, STORE_GET_ORDER_ID)
    should_be_delete_order(logger, STORE_GET_ORDER_ID)
