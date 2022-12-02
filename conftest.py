import pytest
import logging
import os
import shutil
import glob


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


def pytest_sessionstart():
    if os.path.isdir(os.path.dirname(__file__) + '/.pytest_cache'):
        shutil.rmtree(os.path.dirname(__file__) + '/.pytest_cache')
    files = glob.glob('allure-results/*') + glob.glob('logs/*')
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


@pytest.fixture(scope='module')
def logger(request):
    if not os.path.exists(os.path.dirname(__file__) + '/logs'):
        os.mkdir(os.path.dirname(__file__) + '/logs')
    log_path = os.path.dirname(__file__) + r'/logs'
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.DEBUG)
    create_handler = logging.FileHandler(os.path.join(log_path, f'{request.node.module.__name__}.log'))
    create_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s| %(module)s |%(name)s | %(levelname)s | %(message)s')
    create_handler.setFormatter(formatter)
    logger.addHandler(create_handler)
    return logger
