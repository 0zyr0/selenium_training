# Для добавления товара нужно открыть меню Catalog, в правом верхнем углу нажать кнопку "Add New Product",
# заполнить поля с информацией о товаре и сохранить.
#
# Достаточно заполнить только информацию на вкладках General, Information и Prices. Скидки (Campains)
# на вкладке Prices можно не добавлять.
#
# Переключение между вкладками происходит не мгновенно, поэтому после переключения можно
# сделать небольшую паузу (о том, как делать более правильные ожидания, будет рассказано в следующих занятиях).
#
# Картинку с изображением товара нужно уложить в репозиторий вместе с кодом.
# При этом указывать в коде полный абсолютный путь к файлу плохо, на другой машине работать не будет.
# Надо средствами языка программирования преобразовать относительный путь в абсолютный.
#
# После сохранения товара нужно убедиться, что он появился в каталоге (в админке).

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import random
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


def generate_name():
    cache = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] * 10
    random.shuffle(cache)
    buf = ""
    for i in range(0, 10):
        buf += str(cache.pop())

    user = "test" + buf + " order"

    return user


def test_add_order(driver):
    name_order = generate_name()

    test_login(driver)

    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")

    before_add = driver.find_element_by_tag_name("tr[class='footer']").get_property("textContent")

    before_add_re = re.findall(r'(\d+)$', before_add, re.MULTILINE)

    #p = re.match(r'', before_add)

    print(before_add_re[0])

    driver.find_element_by_tag_name("div a[class='button']:nth-child(2)").click()

    driver.find_element_by_name("name[en]").send_keys(name_order)

    driver.find_element_by_name("code").send_keys("test code")

    driver.find_element_by_tag_name("input[type='file']").send_keys(file_path)

    driver.find_element_by_tag_name("ul[class='index'] li:nth-child(2)").click()

    WebDriverWait(driver, 10)

    select_manufacturer = driver.find_element_by_css_selector("select[name='manufacturer_id']")

    Select(select_manufacturer).select_by_value("1")

    driver.find_element_by_name("keywords").send_keys("test")

    driver.find_element_by_name("short_description[en]").send_keys("test")

    driver.find_element_by_tag_name("div[class='trumbowyg-editor']").send_keys("test")

    driver.find_element_by_name("head_title[en]").send_keys("test")

    driver.find_element_by_name("meta_description[en]").send_keys("test")

    driver.find_element_by_tag_name("ul[class='index'] li:nth-child(4)").click()

    WebDriverWait(driver, 10)

    select_price = driver.find_element_by_css_selector("select[name='purchase_price_currency_code']")

    Select(select_price).select_by_value("USD")

    driver.find_element_by_name("prices[USD]").send_keys("17")

    driver.find_element_by_name("prices[EUR]").send_keys("17")

    driver.find_element_by_name("save").click()

    after_add = driver.find_element_by_tag_name("tr[class='footer']").get_property("textContent")

    after_add_re = re.findall(r'(\d+)$', before_add, re.MULTILINE)

    print('Doe')
