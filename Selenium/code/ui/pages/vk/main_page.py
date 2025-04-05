from ui.locators import vk_locators
import allure

from ui.pages.vk.base_page import BasePage
from ui.pages.vk.login_page import LoginPage

class MainPage(BasePage):

    locators = vk_locators.MainPageLocators()
    url = "https://education.vk.company/"

    @allure.step("Open login form")
    def go_to_login_page(self) -> LoginPage:
        open_form_button = self.find(self.locators.LOGIN_BUTTON)
        self.click(open_form_button)
        return LoginPage(self.driver)

    def has_login_button(self) -> bool:
        return self.is_element_present(self.locators.LOGIN_BUTTON)
