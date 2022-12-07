import json
import requests


def put_user(logger, endpoint):
    with open('data/user/put_user.json', 'r') as jf:
        json_file = json.load(jf)
    requests.put(f'{endpoint}', params={'username': 'Dem'}, json=json_file)


def should_be_put_user(logger, endpoint, user_name='NewDem'):
    response_json = requests.get(f'{endpoint}/{user_name}')
    assert response_json.status_code == 200, ('User is not put', logger.error('User is not put'))[0]
    logger.info('User is put')
