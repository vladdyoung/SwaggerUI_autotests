import pytest
import allure
from config import *
from pages.base_page import *
from pages.pet.get_page import *


@allure.feature('Test SwaggerUI')
@allure.story('Pet GET methods')
@allure.title('Test status code all get methods is 200')
@allure.step('Checking that status code all get methods is 200')
@pytest.mark.test_positive_status_code
@pytest.mark.parametrize('endpoint', [PET_GET_AVAILABLE, PET_GET_PENDING, PET_GET_SOLD, PET_GET_ID])
def test_positive_status_code(logger, endpoint):
    should_be_page_is_found(logger, endpoint)


@allure.feature('Test SwaggerUI')
@allure.story('Pet GET methods')
@allure.title('Test content-type')
@allure.step('Checking that content-type all get methods is JSON')
@pytest.mark.test_content_type
@pytest.mark.parametrize('endpoint', [PET_GET_AVAILABLE, PET_GET_PENDING, PET_GET_SOLD, PET_GET_ID])
def test_content_type(logger, endpoint):
    should_be_response_json(logger, endpoint)


@allure.feature('Test SwaggerUI')
@allure.story('Pet GET methods')
@allure.title('Test full response')
@allure.step('Checking that response is full')
@pytest.mark.test_full_response
@pytest.mark.parametrize('endpoint', [PET_GET_AVAILABLE, PET_GET_PENDING, PET_GET_SOLD, PET_GET_ID])
def test_full_response(logger, endpoint):
    should_be_full_response(logger, endpoint)


@allure.feature('Test SwaggerUI')
@allure.story('Pet GET methods')
@allure.title('Test get PetId')
@allure.step('Checking that method get PetId is work')
@pytest.mark.chack_equals_jsons_get
def test_get_pet_id(logger):
    should_be_get_pet_id(logger, PET_GET_ID)
