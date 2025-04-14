import pytest

from ui.fixtures import *
from ui.pages.vk.feed_page import FeedPage
from ui.pages.vk.main_page import MainPage
from ui.pages.vk.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://www.python.org')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
    }

@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def feed_page(driver):
    return FeedPage(driver=driver)
