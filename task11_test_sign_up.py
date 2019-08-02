import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


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


def generate_email():
    cache = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] * 10
    random.shuffle(cache)
    buf = ""
    for i in range(0, 10):
        buf += str(cache.pop())

    user = "test" + buf + "@mail.org"

    return user


# def test_check_email(driver):
#     test_login(driver)
#
#     driver.get("http://localhost/litecart/admin/")
#
#     elements = driver.find_elements_by_css_selector("li#app-")
#
#     driver.find_elements_by_id("app-")[4].click()
#
#     customers = driver.find_elements_by_css_selector("tr.row")
# 
#     email_list = []
#
#     for i, customer in enumerate(customers):
#
#         driver.find_elements_by_css_selector("tr.row td a i")[i].click()
#
#         verify_email = driver.find_element_by_name("email").get_attribute('value')
#
#         email_list.append(verify_email)
#
#         driver.find_element_by_name("cancel").click()
#
#     return email_list


def test_sign_up(driver):
    email = generate_email()

    password = 'test'

    test_login(driver)

    driver.get("http://localhost/litecart/en/")

    driver.find_element_by_css_selector("tr:nth-child(5)").click()

    driver.find_element_by_name("firstname").send_keys("test")

    driver.find_element_by_name("lastname").send_keys("test")

    driver.find_element_by_name("address1").send_keys("test")

    driver.find_element_by_name("postcode").send_keys("12345")

    driver.find_element_by_name("city").send_keys("test")

    # select_country = driver.find_element_by_css_selector("span[class='select2-selection select2-selection--single']")

    select_country = driver.find_element_by_css_selector("select[name='country_code']")

    Select(select_country).select_by_value("US")

    driver.find_element_by_name("email").send_keys(email)

    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("confirmed_password").send_keys(password)

    driver.find_element_by_name("phone").send_keys("+1")

    driver.find_element_by_name("create_account").click()

    # WebDriverWait(driver, 10)

    zone = driver.find_element_by_css_selector("select[name='zone_code']")

    Select(zone).select_by_value("AL")

    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("confirmed_password").send_keys(password)

    driver.find_element_by_name("create_account").click()

    WebDriverWait(driver, 10)

    driver.find_element_by_tag_name("div[class='content'] ul[class='list-vertical'] li a[href = 'http://localhost/litecart/en/logout']").click()

    driver.find_element_by_name('email').send_keys(email)

    driver.find_element_by_name('password').send_keys(password)

    driver.find_element_by_name('login').click()

    driver.find_element_by_tag_name("div[class='content'] ul[class='list-vertical'] li a[href = 'http://localhost/litecart/en/logout']").click()
