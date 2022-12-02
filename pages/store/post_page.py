import json
import requests


def create_order(logger, endpoint):
    with open('data/store/post_order.json', 'r') as jf:
        json_file = json.load(jf)
    requests.post(endpoint, json=json_file)


def should_be_create_order(logger, endpoint, createid=7):
    response_json = requests.get(f'{endpoint}/{createid}').json()
    with open('data/store/post_order.json', 'r') as jf:
        json_file = json.load(jf)
    assert response_json == json_file, ('Order is not created', logger.error('Order is not created'))[0]
    logger.info('Order is not created')
