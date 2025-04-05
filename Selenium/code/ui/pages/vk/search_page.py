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
