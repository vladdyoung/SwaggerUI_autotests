import requests
import json


def should_be_get_pet_id(logger, endpoint):
    with open('data/pet/pet_get_id.json', 'r') as jf:
        json_file = json.load(jf)
    response_json = requests.get(endpoint).json()
    assert response_json == json_file, ('PetId is not added', logger.error('PetId is not added'))[0]
    logger.info('PetId is added')

