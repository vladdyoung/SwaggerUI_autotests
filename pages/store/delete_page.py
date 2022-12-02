import requests


def delete_order(logger, endpoint, orderid=7):
    requests.delete(f'{endpoint}/{orderid}')


def should_be_delete_order(logger, endpoint, orderid=7):
    response_deleted_pet = requests.get(f'{endpoint}/{orderid}')
    assert response_deleted_pet.status_code == 404,\
        ('Order is not deleted', logger.error('Order is not deleted'))[0]
    logger.info('Order is not deleted')
