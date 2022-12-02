import requests


def delete_pet(logger, endpoint, petid=345):
    requests.delete(f'{endpoint}/{petid}')


def should_be_delete_pet(logger, endpoint, petid=345):
    response_deleted_pet = requests.get(f'{endpoint}/{petid}')
    assert response_deleted_pet.status_code == 404,\
        ('Pet is not deleted', logger.error('Pet is not deleted'))[0]
    logger.info('Pet is deleted')
