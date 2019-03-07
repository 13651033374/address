from page.addcontact_page import AddContact
from page.addressbook_page import AddressBook
from page.savepage import SavePage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def addressbook(self):
        return AddressBook(self.driver)
    @property
    def save(self):
        return SavePage(self.driver)

    @property
    def addcontact(self):
        return AddContact(self.driver)