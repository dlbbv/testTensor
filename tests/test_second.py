import requests
from time import sleep
from selenium.webdriver.common.by import By

from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.constants.constants import *


def test_getting_posts():
    response = requests.get(url=SBIS_URL)
    assert response.status_code == 200, 'ERR'


def test_click_contacts(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open()
    sbis_page.findLinkContacts()


def test_region(browser):
    sbis_page = SbisPage(browser)
    sbis_page.checkRegion(MY_REGION)


def test_partners(browser):
    sbis_page = SbisPage(browser)
    sbis_page.checkPartners()


def test_change_region(browser):
    sbis_page = SbisPage(browser)
    sbis_page.changeRegion()


def test_check_change_region(browser):
    sbis_page = SbisPage(browser)
    sbis_page.checkRegion(NEW_REGION)


def test_check_change_title(browser):
    sbis_page = SbisPage(browser)
    sbis_page.checkTitle()


def test_check_change_url(browser):
    sbis_page = SbisPage(browser)
    sbis_page.checkUrl()


def test_check_change_partners(browser):
    sbis_page = SbisPage(browser)
    sbis_page.checkPartners()

