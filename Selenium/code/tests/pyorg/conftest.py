import pytest
from ui.pages.python.base_page import BasePage
from ui.pages.python.main_page import MainPage

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)
