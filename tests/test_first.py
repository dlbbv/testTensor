import requests
from time import sleep
from selenium.webdriver.common.by import By

from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.constants.constants import SBIS_URL


def test_getting_posts():
    response = requests.get(url=SBIS_URL)
    assert response.status_code == 200, 'ERR'


def test_click_contacts(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open()
    sbis_page.findLinkContacts()


def test_click_tenzor(browser):
    tensor_page = TensorPage(browser)
    tensor_page.findImgTensor()
    sleep(5)
    browser.switch_to.window(browser.window_handles[-1])


def test_find_block(browser):
    tensor_page = TensorPage(browser)
    tensor_page.findBlock()


def test_click_about(browser):
    tensor_page = TensorPage(browser)
    tensor_page.findAbout()


def test_img_size(browser):
    tensor_page = TensorPage(browser)
    tensor_page.checkPhotoSize()


