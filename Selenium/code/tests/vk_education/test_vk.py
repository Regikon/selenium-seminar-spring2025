from typing import Tuple
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver

from ui.pages.vk.feed_page import FeedPage
from ui.pages.vk.login_page import LoginPage
from ui.pages.vk.main_page import MainPage
import os


class BaseCase:
    authorize = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, credentials, request: FixtureRequest):
        self.driver: WebDriver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            (email, password) = credentials
            self.login_page.login(email, password)


class NoCredentialsGiven(Exception):
    pass

@pytest.fixture(scope='session')
def credentials() -> Tuple[str, str]:
    CREDENTIAL_PATH = "./files/credentials/vk_login"
    if not os.path.exists(CREDENTIAL_PATH):
        raise NoCredentialsGiven
    with open(CREDENTIAL_PATH , "r") as cred_file:
        line = cred_file.readline().strip().split()
        email, password = line[0], line[1]
        return email, password

class TestLogin(BaseCase):
    authorize = False

    SESSION_COOKIE_NAME = "sessionid_gtp"

    def test_logins_successfully(self, credentials):
        email, password = credentials
        self.login_page.login(email, password)

    def test_redirects_to_feed_page(self, credentials):
        self.login_page.login(*credentials)
        assert(self.driver.current_url == FeedPage.url)

    def test_hides_login_button(self, credentials):
        self.login_page.login(*credentials)
        self.driver.get(MainPage.url)
        main_page = MainPage(driver=self.driver)
        assert(not main_page.has_login_button())

    def test_puts_session_cookie(self, credentials):
        self.login_page.login(*credentials)
        cookie = self.driver.get_cookie(self.SESSION_COOKIE_NAME)
        assert(cookie is not None)

class TestSearchPeople(BaseCase):
    authorize = True

