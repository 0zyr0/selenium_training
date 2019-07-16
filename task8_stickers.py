import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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
    #wait.until(EC.title_is("My Store"))


def test_check_stickers(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/en/")

    elements = driver.find_elements_by_css_selector("div.content div.box div.image-wrapper")

    for i, element in enumerate(elements):
        element = driver.find_elements_by_tag_name("div.sticker")[i]
        # element = driver.find_element_by_css_selector("div.sticker")
        assert element
        print(element)

