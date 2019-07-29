import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re



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


def test_check_sort1(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    elements = driver.find_elements_by_css_selector("tr.row")

    original_list_country_names = []

    sorted_list_country_names = []

    for i, element in enumerate(elements):
        original_list_country_names.append(re.match(r'^\d+\s*\w{2}\s*(.+)\d+$', element.text)[1].strip())

        sorted_list_country_names.append(re.match(r'^\d+\s*\w{2}\s*(.+)\d+$', element.text)[1].strip())

    print(original_list_country_names, '\n')

    sorted_list_country_names.sort()

    print(sorted_list_country_names, '\n')

    if original_list_country_names[i] == sorted_list_country_names[i]:
        print('Countries sorted by Aa..Zz', '\n')
    else:
        print(original_list_country_names[i], ' not equals ', sorted_list_country_names[i], '\n')



    print('Test Sort Country names has done')


def test_check_sort2(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    elements = driver.find_elements_by_css_selector("div.content div.box div.image-wrapper")

    for i, element in enumerate(elements):
        element = driver.find_elements_by_tag_name("div.sticker")[i]
        # element = driver.find_element_by_css_selector("div.sticker")
        assert element
        print(element)

