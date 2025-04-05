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
    FULL_NAME = "Олег Музалев"
    POSITIVE_QUERY = "Музалев"
    NEGATIVE_QUERY = "12038гысмджлтфыджво"
    driver: WebDriver

    def test_searches_human(self, feed_page: FeedPage):
        search_page = feed_page.search(self.POSITIVE_QUERY)
        assert(search_page.contains_entry_with_name(self.FULL_NAME))
        assert(not search_page.has_nothing_found_caption())

    def test_shows_caption_if_nothing_found(self, feed_page: FeedPage):
        search_page = feed_page.search(self.NEGATIVE_QUERY)
        assert(not search_page.has_found())
        assert(search_page.has_nothing_found_caption())

class TestSearchSeminar(BaseCase):
    authorize = True
    QUERY = 'selenium'
    TRUE_NAME = 'Автоматизация тестирования'

    def test_finds_seminar(self, feed_page: FeedPage):
        search_page = feed_page.search(self.QUERY)
        search_page.select_lessons()
        lesson = search_page.find_lesson_by_name(self.TRUE_NAME)
        assert(lesson is not None)
        assert(lesson.text == self.TRUE_NAME)
