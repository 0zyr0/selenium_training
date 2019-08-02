import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    # создание драйвера. Инициализация браузера
    wd = webdriver.Chrome()
    #wd = webdriver.Chrome("D:/python_selenium_test/chromedriver_win32/chromedriver.exe")
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_check_stickers(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/en/")

    elements = driver.find_elements_by_css_selector("div.content div.box div.image-wrapper")

    a_elements = driver.find_elements_by_class_name("product")

    stickers = []

    for i, element in enumerate(a_elements):

        sticker = driver.find_elements_by_tag_name("div.sticker")[i]

        stickers.append(sticker)

        if sticker == stickers[i]:
            print("Element have one sticker")
