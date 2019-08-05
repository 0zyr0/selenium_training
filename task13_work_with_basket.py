# Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
#
# 3) подождать, пока счётчик товаров в корзине обновится
# 4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
# 5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
# 6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


file_path = os.path.abspath('D:/work/github/zms_selenium_training/selenium_training/files/donald.jpg')


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


def test_basket(driver):

    test_login(driver)

    driver.get("http://litecart.stqa.ru/en/")

    #for i in range(3):

    driver.find_element_by_tag_name("div[class='image-wrapper'] img.image:nth-child(1)").click()

    driver.find_element_by_name("add_cart_product").click()

    # driver.find_element_by_tag_name("span[class='quantity']")

    driver.implicitly_wait(5000)

    driver.find_element_by_tag_name("i[class='fa fa-home']").click()

    driver.find_element_by_tag_name("a[href='http://litecart.stqa.ru/en/checkout'][class='link']").click()

    for i in range(3):

        driver.find_element_by_tag_name("button[value='Remove']")

        driver.implicitly_wait(20)
