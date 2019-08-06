# Сделайте сценарий, который проверяет, что ссылки на странице редактирования страны открываются в новом окне.
#
# 4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой -- они ведут на внешние страницы
# и открываются в новом окне, именно это и нужно проверить.
#
#  Конечно, можно просто убедиться в том, что у ссылки есть атрибут target="_blank".
#  Но в этом упражнении требуется именно кликнуть по ссылке, чтобы она открылась в новом окне,
#  потом переключиться в новое окно, закрыть его, вернуться обратно, и повторить эти действия для всех таких ссылок.
#
#     Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна.

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


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


def switch_win(driver, all_window, current_window):
    for window in all_window:

        if current_window == window:
            all_window.remove(window)

    c_window = all_window[0]

    driver.switch_to_window(c_window)

    WebDriverWait(driver, 15)

    driver.close()

    WebDriverWait(driver, 15)

    driver.switch_to_window(current_window)


def test_open_window(driver):
    test_login(driver)

    driver.get("http://localhost/litecart/admin/")

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=countries&doc=edit_country']").click()

    all_links = driver.find_elements_by_tag_name("a[target='_blank'] i[class='fa fa-external-link']")

    for i, element in enumerate(all_links):

        driver.find_elements_by_tag_name("a[target='_blank'] i[class='fa fa-external-link']")[i].click()

        WebDriverWait(driver, 15)

        all_windows = driver.window_handles

        current_window = driver.current_window_handle

        switch_win(driver, all_windows, current_window)
