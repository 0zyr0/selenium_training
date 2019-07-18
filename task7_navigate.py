import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    # создание драйвера. Инициализация браузера
    #wd = webdriver.Chrome("D:/python_selenium_test/chromedriver_win32/chromedriver.exe")
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(10)
    #wait.until(EC.title_is("My Store"))


def test_left_frame_click(driver):
    test_login(driver)

    elements = driver.find_elements_by_css_selector("li#app-")

    for i, element in enumerate(elements):

        driver.find_elements_by_id("app-")[i].click()
        element_h1 = driver.find_element_by_tag_name('h1')
        assert element_h1

        sub_elements = driver.find_elements_by_tag_name("ul.docs li")

        for j, sub_element in enumerate(sub_elements):
            driver.find_elements_by_tag_name("ul.docs li")[j].click()
            sub_element_h1 = driver.find_element_by_tag_name('h1')
            assert sub_element_h1
