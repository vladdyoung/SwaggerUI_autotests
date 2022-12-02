import requests
import json


def should_be_get_inventory(logger, endpoint):
    with open(r'D:\PycharmProjects\SwaggerUI_autotests\data\store\get_inventory.json', 'r') as jf:
        json_file = json.load(jf)
    response_json = requests.get(endpoint).json()
    requests.get(endpoint).json()
    assert response_json == json_file, ('Empty response', logger.error('Empty response'))[0]
    logger.info('Empty response')

