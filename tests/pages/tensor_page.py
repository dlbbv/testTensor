from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage
from pages.constants.constants import *


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def findImgTensor(self):
        assert self.find(IMG_TENSOR), 'Изображение Тензор не найдено'
        img_tensor = self.find(IMG_TENSOR)
        return img_tensor.click()

    def findBlock(self):
        assert self.find(BLOCK_SELECTOR), 'Блок "Сила в людях" не найден'

    def findAbout(self):
        block_pip = self.find(BLOCK_SELECTOR)
        link_more = block_pip.find_element(By.LINK_TEXT, TEXT_MORE)
        self.execute(args=(LINK_SCRIPT, link_more))
        assert self.currentUrl() == URL_ABOUT, f'Вместо {URL_ABOUT} открывается {self.currentUrl()}'

    def checkPhotoSize(self):
        images = self.findAll(IMG_BLOCK)
        first_img_size = images[0].size
        for img in images[1:]:
            img_size = img.size
            assert img_size == first_img_size, f"Размеры фотографии {img.get_attribute('src')} не совпадают с первой фотографией"
