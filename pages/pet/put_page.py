import json
import requests


def put_pet(logger, endpoint):
    with open('data/pet/put_pet.json', 'r') as jf:
        json_file = json.load(jf)
    requests.put(f'{endpoint}', json=json_file)


def should_be_put_pet(logger, endpoint, petid=346):
    with open('data/pet/put_pet.json', 'r') as jf:
        json_file = json.load(jf)
    response_json = requests.get(f'{endpoint}/{petid}').json()
    assert response_json == json_file,\
        ('PetId is not added', logger.error('PetId is not added'))[0]
    logger.info('PetId is added')
