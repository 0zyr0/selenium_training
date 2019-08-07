# Переделайте созданный в задании 13 сценарий для добавления товаров в корзину и удаления товаров из корзины, чтобы он использовал многослойную архитектуру.
#
# А именно, выделите вспомогательные классы для работы с главной страницей (откуда выбирается товар),
# для работы со страницей товара (откуда происходит добавление товара в корзину), со страницей корзины (откуда происходит удаление),
# и реализуйте сценарий, который не напрямую обращается к операциям Selenium, а оперирует вышеперечисленными объектами-страницами.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


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


def test_basket(driver):
    wait = WebDriverWait(driver, 15)

    test_login(driver)

    driver.get("http://litecart.stqa.ru/en/")

    for i in range(4):

        driver.find_element_by_tag_name("div[class='image-wrapper'] img.image:nth-child(1)").click()

        try:
            select_size = driver.find_element_by_css_selector("select[name='options[Size]']")

            Select(select_size).select_by_value("Small")

        except NoSuchElementException:
            True

        driver.find_element_by_name("add_cart_product").click()

        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "span[class='quantity']"), str(i)))

        driver.find_element_by_tag_name("i[class='fa fa-home']").click()

    driver.find_element_by_tag_name("a[href='http://litecart.stqa.ru/en/checkout'][class='link']").click()

    for i in range(4):
        driver.find_element_by_tag_name("button[value='Remove']").click()

        wait.until(EC.invisibility_of_element((By.TAG_NAME, "li[class='shortcut']")))
