from selenium.webdriver.common.by import By


IMG_TENSOR = (By.XPATH, "//img[@alt='Разработчик системы СБИС — компания «Тензор»']")
BLOCK_SELECTOR = (By.CLASS_NAME, "tensor_ru-Index__block4-content")
TEXT_MORE = "Подробнее"
LINK_SCRIPT = "arguments[0].click();"
URL_ABOUT = 'https://tensor.ru/about'
SBIS_URL = 'https://sbis.ru/'
LINK_CONTACTS = (By.LINK_TEXT, "Контакты")
IMG_BLOCK = (By.XPATH, "//div[@class='tensor_ru-About__block3-image-wrapper']")
REGION_SELECTOR = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
MY_REGION = 'Нижегородская обл.'
NEW_REGION_SELECTOR = (By.XPATH, "//span[@title='Камчатский край']")
NEW_REGION = 'Камчатский край'
NEW_REGION_URL = '41-kamchatskij-kraj'
PARTNERS_SELECTOR = (By.ID, "contacts_list")