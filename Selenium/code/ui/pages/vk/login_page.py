from ui.pages.vk.base_page import BasePage
from ui.locators.vk_locators import LoginFormLocators
from ui.pages.vk.feed_page import FeedPage

class LoginPage(BasePage):
    locators = LoginFormLocators
    url = "https://education.vk.company/#auth-vk-id"

    def login(self, email: str, password: str):
        self.click(self.locators.LOGIN_VIA_EMAIL_BUTTON)
        email_field = self.find(self.locators.EMAIL_FIELD)
        password_field = self.find(self.locators.PASSWORD_FIELD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        self.click(self.locators.LOGIN_BUTTON)
        return FeedPage(driver=self.driver)
