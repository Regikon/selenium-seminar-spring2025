from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, "вход / регистрация")

class LoginFormLocators:
    LOGIN_VIA_EMAIL_BUTTON = (By.CSS_SELECTOR, "button.gtm-signup-modal-link")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.gtm-login-btn")

