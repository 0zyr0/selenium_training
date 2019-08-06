# Сделайте сценарий, который проверяет, не появляются ли в логе браузера сообщения при открытии страниц в учебном приложении,
# а именно -- страниц товаров в каталоге в административной панели.
#
# Сценарий должен состоять из следующих частей:
#
# 3) последовательно открывать страницы товаров и проверять, не появляются ли в логе браузера сообщения (любого уровня)

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


@pytest.fixture
def driver(request):
    # создание драйвера. Инициализация браузера
    wd = webdriver.Chrome()
    # wd = webdriver.Chrome("D:/python_selenium_test/chromedriver_win32/chromedriver.exe")
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    # wait.until(EC.title_is("My Store"))


def test_log_browser(driver):
    test_login(driver)

    driver.get("http://localhost/litecart/admin/")

    driver.find_element_by_tag_name("li#app-:nth-child(2)").click()

    driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1']").click()

