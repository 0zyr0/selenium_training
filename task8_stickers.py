import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


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


def check_exists_by_xpath(xpath):
    return len(webdriver.find_elements_by_xpath(xpath)) > 0



def test_check_stickers(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/en/")

    lists = driver.find_elements_by_css_selector("div#box-most-popular li")

    for list in lists:
        sticker = list.find_element_by_xpath(".//div[@class='image-wrapper']/div")
        check_exists_by_xpath(sticker)
        print(sticker)
        #sticker.get_attribute()
        # sticker = list.find_element_by_xpath(".//div[@class='sticker new']/")
    #    lists.get_attribute("div.image-wrapper div")[list]

    #driver.find_elements_by_css_selector("div.box-most-popular li").get_attribute()
    #check_exists_by_xpath('.//*[@id="box-most-popular"]/div/ul/li[1]/a[1]/div[1]/div')

    # driver.find_element_by_name("username").send_keys("admin")
    # driver.find_element_by_name("password").send_keys("admin")
    # driver.find_element_by_name("login").click()