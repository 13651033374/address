from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavePage(BaseAction):
    bendi = By.XPATH,'//*[@text="本地保存"]'
    def click_bendi(self):
        self.click(self.bendi)