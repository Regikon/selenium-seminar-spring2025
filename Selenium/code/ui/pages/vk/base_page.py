import time
from typing import List

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass

class BasePage(object):

    url = ''

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.__trim_query(self.driver.current_url) == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.is_opened()

    def wait(self, timeout=None) -> WebDriverWait:
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_many(self, locator, timeout=None) -> List[WebElement]:
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator, timeout=None): 
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def is_element_present(self, locator, timeout=15) -> bool:
        try: 
            self.find(locator, timeout)
            return True
        except Exception:
            return False

    def __trim_query(self, url: str) -> str:
        query_start = url.find('?')
        if query_start > 0:
            return url[:query_start]
        return url
