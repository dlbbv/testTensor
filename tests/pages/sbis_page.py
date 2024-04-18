from time import sleep

from pages.base_page import BasePage
from pages.constants.constants import *


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(SBIS_URL)

    def findLinkContacts(self):
        assert self.find(LINK_CONTACTS), f'Кнопка {LINK_CONTACTS[1]} не найдена'
        link_contacts = self.find(LINK_CONTACTS)
        link_contacts.click()


    def checkRegion(self, region):
        region_block = self.find(REGION_SELECTOR)
        assert region_block.text == region, f'Определяется регион {region_block.text} вместо {region}'

    def changeRegion(self):
        region_block = self.find(REGION_SELECTOR)
        region_block.click()
        sleep(5)
        new_region = self.find(NEW_REGION_SELECTOR)
        new_region.click()
        sleep(5)

    def checkTitle(self):
        assert NEW_REGION in self.title(), f'В title "{self.title()} не {NEW_REGION}"'

    def checkUrl(self):
        assert NEW_REGION_URL in self.currentUrl(), f'В url "{self.currentUrl()} не {NEW_REGION_URL}"'

    def checkPartners(self):
        assert self.find(PARTNERS_SELECTOR), 'Блок партнеров не найден'