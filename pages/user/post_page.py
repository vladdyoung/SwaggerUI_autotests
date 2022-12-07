import json
import requests


def create_user(logger, endpoint):
    with open('data/user/post_create_user.json', 'r') as jf:
        json_file = json.load(jf)
    requests.post(endpoint, json=json_file)


def should_be_create_user(logger, endpoint, user_name='Dem'):
    response_json = requests.get(f'{endpoint}/{user_name}').json()
    with open('data/user/post_create_user.json', 'r') as jf:
        json_file = json.load(jf)
    assert response_json == json_file, ('User is not create', logger.error('User is not create'))[0]
    logger.info('User is create')


def should_be_create_user_with(logger, endpoint):
    with open('data/user/post_create_with_array.json', 'r') as jf:
        json_file = json.load(jf)
    response_json = requests.post(endpoint, json=json_file)
    assert response_json.status_code == 200, ('Not created', logger.error('Not created'))[0]
    logger.info('Successfully create')


