import json
import requests


def should_be_upload_image(logger, endpoint):
    data = {'petId': 2, 'additionalMetadata': 'cat'}
    image = {'file': open('data/pet/cat.jpg', 'rb')}
    try:
        with open('data/pet/cat.json', 'r') as jf:
            json_file = json.load(jf)
        response_json = requests.post(endpoint, data=data, files=image)
        assert response_json.json() == json_file, \
            ('Wrong! JSONs is not equal', logger.error('Wrong! JSONs is not equal'))[0]
        logger.info('OK! JSONs is equal')
    except:
        logger.error(f'Wrong endpoint {endpoint}', exc_info=True)
        raise AssertionError(f'Wrong endpoint {endpoint}')


def add_new_pet(logger, endpoint):
    with open('data/pet/post_add_new_pet_id.json', 'r') as jf:
        json_file = json.load(jf)
    requests.post(endpoint, json=json_file)


def should_be_added_new_pet_id(logger, endpoint, petid=345):
    response_json = requests.get(f'{endpoint}/{petid}').json()
    with open('data/pet/post_add_new_pet_id.json', 'r') as jf:
        json_file = json.load(jf)
    assert response_json == json_file, ('PetId is not added', logger.error('PetId is not added'))[0]
    logger.info('PetId is added')


def update_pet_name(logger, endpoint, petid=345):
    data = {'petId': 345, 'name': 'NEW_NAME', 'status': 'pending'}
    requests.post(f'{endpoint}/{petid}', data=data)


def should_be_update_pet(logger, endpoint, petid=345):
    response_json = requests.get(f'{endpoint}/{petid}').json()
    assert response_json['name'] == 'NEW_NAME' and response_json['status'] == 'pending', \
        ('PetId is not added', logger.error('PetId is not added'))[0]
    logger.info('PetId is added')
