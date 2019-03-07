from base.base_driver import init_driver
from page.page import Page


class TestContact():
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()
    def testcontact(self):
        self.page.addressbook.click_addpeople()
        self.page.save.click_bendi()
        self.page.addcontact.keyword_addname('zhangsan')
        self.page.addcontact.keyword_addtel('188888')
        self.page.addcontact.clickmore()