from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressBook(BaseAction):
    addpeople_button = By.CLASS_NAME,'android.widget.ImageButton'
    def click_addpeople(self):
        self.click(self.addpeople_button)