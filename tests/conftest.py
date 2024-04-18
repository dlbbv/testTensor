import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument(r'--user-data-dir=C:\Users\tooch\PycharmProjects\test1\Chrome\User Data')
    # options.add_argument('--profile-directory=Profile 1')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()