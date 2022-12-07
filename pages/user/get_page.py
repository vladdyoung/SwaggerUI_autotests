import requests


def should_be_user_login(logger, endpoint):
    params = {'username': 'Dem', 'password': 'pass'}
    response_json = requests.get(endpoint, params=params)
    assert response_json.status_code == 200, ('Login mistake', logger.error('Login mistake'))[0]
    logger.info('Login successful')


def should_be_user_logout(logger, endpoint):
    response_json = requests.get(endpoint)
    assert response_json.status_code == 200, ('Logout mistake', logger.error('Logout mistake'))[0]
    logger.info('Logout successful')
