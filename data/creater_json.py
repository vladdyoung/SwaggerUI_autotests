import json
import requests


def create_json(url, json_name):
    json_obj = requests.get(url, timeout=5).json()
    with open(f'{json_name}.json', 'w') as json_file:
        json.dump(json_obj, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    create_json(url='https://petstore.swagger.io/v2/store/inventory', json_name='store_get_inventory')
