import pytest
import allure
from config import *
from pages.pet.put_page import *


@allure.feature('Test SwaggerUI')
@allure.story('Pet PUT method')
@allure.title('Test update pet')
@allure.step('Checking that pet is update')
@pytest.mark.test_put_pet
def test_put_pet(logger):
    put_pet(logger, PET_PUT)
    should_be_put_pet(logger, PET_PUT)
