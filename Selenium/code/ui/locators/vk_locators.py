from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, "вход / регистрация")

class LoginFormLocators:
    LOGIN_VIA_EMAIL_BUTTON = (By.CSS_SELECTOR, "button.gtm-signup-modal-link")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.gtm-login-btn")

class FeedPageLocators:
    SHOW_SEARCH_BUTTON = (By.CSS_SELECTOR, "li.js-show-search > a")
    SEARCH_FIELD = (By.XPATH, '//li[@class="js-search-input"]/form/input')
    NEW_DESING_CLOSE_NAG = (By.CLASS_NAME, 'cancel-btn')

class SearchPageLocators:
    SEARCH_RESULT_ENTRY = (By.CSS_SELECTOR, 'td.cell-name')
    ENTRY_NAME = (By.CLASS_NAME, 'realname')
    NOT_FOUND_CAPTION = (By.CLASS_NAME, 'search-warning')
    WORD_IN_ENTRY_NAME = (By.CLASS_NAME, 'accent')
