import pytest
import allure
from config import *
from pages.pet.delete_page import *
from pages.pet.post_page import *


@allure.feature('Test SwaggerUI')
@allure.story('Pet DELETE method')
@allure.title('Test delete pet')
@allure.step('Checking that pet is delete')
@pytest.mark.test_delete_pet
def test_delete_pet(logger):
    add_new_pet(logger, PET_POST_ADD_NEW_PET)
    should_be_added_new_pet_id(logger, PET_POST_ADD_NEW_PET)
    delete_pet(logger, PET_DELETE, petid=345)
    should_be_delete_pet(logger, PET_DELETE)
