from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddContact(BaseAction):
    addname = By.XPATH,'//*[@text="姓名"]'
    addtel = By.XPATH,'//*[@text="电话"]'
    more = By.XPATH,'//*[@content-desc="更多选项"]'
    def keyword_addname(self,name):
        self.input(self.addname,name)
    def keyword_addtel(self,tel):
        self.input(self.addtel,tel)
    def clickmore(self):
        self.click(self.more)