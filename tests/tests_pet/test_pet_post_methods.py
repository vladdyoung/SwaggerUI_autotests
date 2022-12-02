import pytest
import allure
from config import *
from pages.pet.post_page import *


@allure.feature('Test SwaggerUI')
@allure.story('Pet POST methods')
@allure.title('Test upload image')
@allure.step('Checking that image is upload')
@pytest.mark.test_upload_image
def test_upload_image(logger):
    should_be_upload_image(logger, PET_POST_UPLOAD_IMAGE)


@allure.feature('Test SwaggerUI')
@allure.story('Pet POST methods')
@allure.title('Test add new pet')
@allure.step('Checking that add new pet')
@pytest.mark.test_add_new_pet
def test_add_new_pet(logger):
    add_new_pet(logger, PET_POST_ADD_NEW_PET)
    should_be_added_new_pet_id(logger, PET_POST_ADD_NEW_PET)


@allure.feature('Test SwaggerUI')
@allure.story('Pet POST methods')
@allure.title('Test update name of pet')
@allure.step('Checking that name is update')
@pytest.mark.test_update_name
def test_update_name(logger):
    add_new_pet(logger, PET_POST_ADD_NEW_PET)
    should_be_added_new_pet_id(logger, PET_POST_ADD_NEW_PET)
    update_pet_name(logger, PET_POST_ADD_NEW_PET)
    should_be_update_pet(logger, PET_POST_ADD_NEW_PET)
