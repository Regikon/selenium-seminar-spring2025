from typing import Union

from selenium.webdriver.remote.webelement import WebElement
from ui.pages.vk.base_page import BasePage
from ui.locators.vk_locators import SearchPageLocators

class SearchPage(BasePage):
    url = "https://education.vk.company/search/"
    locators = SearchPageLocators

    NOTNING_FOUND = "Поиск в этой категории не дал результатов"

    def contains_entry_with_name(self, name: str):
        entries = self.find_many(self.locators.SEARCH_RESULT_ENTRY, 10)
        for entry in entries:
            entry_name = entry.find_element(*self.locators.ENTRY_NAME).text
            if entry_name.strip() == name:
                return True
        return False

    def has_nothing_found_caption(self) -> bool:
        return (self.is_element_present(self.locators.NOT_FOUND_CAPTION) and
                self.find(self.locators.NOT_FOUND_CAPTION).text == self.NOTNING_FOUND)

    def has_found(self) -> bool:
        return self.is_element_present(self.locators.SEARCH_RESULT_ENTRY)

    def select_lessons(self):
        self.click(self.locators.LESSONS_BUTTON)

    def find_lesson_by_name(self,name: str, timeout=15) -> Union[WebElement, None]:
        lesson_names = self.find_many(self.locators.LESSON_NAME)
        for lesson_name in lesson_names:
            if name == lesson_name.text:
                return lesson_name
        return None

