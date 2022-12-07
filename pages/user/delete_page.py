import requests


def delete_user(logger, endpoint, user_name='Dem'):
    requests.delete(f'{endpoint}/{user_name}')


def should_be_delete_user(logger, endpoint, user_name='Dem'):
    response_deleted_pet = requests.get(f'{endpoint}/{user_name}')
    assert response_deleted_pet.status_code == 404,\
        ('User is not deleted', logger.error('User is not deleted'))[0]
    logger.info('User is deleted')
