import pytest

from ui.pages.vk.main_page import MainPage
from ui.pages.vk.login_page import LoginPage


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)
