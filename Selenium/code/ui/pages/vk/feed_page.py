
from ui.pages.vk.base_page import BasePage
from ui.locators.vk_locators import FeedPageLocators
from selenium.webdriver.common.keys import Keys

from ui.pages.vk.search_page import SearchPage

class FeedPage(BasePage):
    url = "https://education.vk.company/feed/"
    locators = FeedPageLocators

    def __init__(self, driver):
        super().__init__(driver)
        # To prevent nag screen randomly appearing
        if self.is_element_present(self.locators.NEW_DESING_CLOSE_NAG):
            self.click(self.locators.NEW_DESING_CLOSE_NAG)

    def search(self, query: str):
        self.click(self.locators.SHOW_SEARCH_BUTTON, 3)
        input = self.find(self.locators.SEARCH_FIELD)
        input.send_keys(query)
        input.send_keys(Keys.RETURN)
        return SearchPage(self.driver)
