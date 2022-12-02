import requests


def should_be_page_is_found(logger, endpoint):
    assert requests.get(endpoint).status_code == 200, \
        ('Response status code is not 200', logger.error('Response status code is not 200'))[0]
    logger.info('OK! Response status code is 200')


def should_be_response_json(logger, endpoint):
    response = requests.get(endpoint)
    assert response.headers['content-type'] == 'application/json', \
        ('Response does not contains JSON', logger.error('Response does not contains JSON'))[0]
    logger.info('Response does not contains JSON')


def should_be_full_response(logger, endpoint):
    length = len(requests.get(endpoint).json())
    assert length > 0, ('Response is empty', logger.error('Response is empty'))[0]
    logger.info('Response is empty')
