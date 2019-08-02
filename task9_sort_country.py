import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


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


def checking_sorting(array1, array2):
    k = len(array1)

    for i in range(k):
        if array1[i] == array2[i]:
            print('Elements sorted by Aa..Zz', '\n')
        else:
            print(array1[i], ' not equals ', array2[i], '\n')


def loop_for_zones_edit(elem, original_list, sorted_list, length):

    for i, el in enumerate(elem):

        original_list.append(re.match(r'^\d+\s+\w{2}\s*(.*)$', el.text)[1].strip())

        sorted_list.append(re.match(r'^\d+\s+\w{2}\s*(.*)$', el.text)[1].strip())

        if i == length:
            break


def loop_for_zones(el, o_list, sorted_list):
    for i, element3 in enumerate(el):
        o_list.append(element3.get_property('text'))

        sorted_list.append(element3.get_property('text'))


def test_check_sort1(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    elements = driver.find_elements_by_css_selector("tr.row")

    original_list_country_names = []

    sorted_list_country_names = []

    for i, element in enumerate(elements):
        original_list_country_names.append(re.match(r'^\d+\s*\w{2}\s*(.+)\d+$', element.text)[1].strip())

        sorted_list_country_names.append(re.match(r'^\d+\s*\w{2}\s*(.+)\d+$', element.text)[1].strip())

    sorted_list_country_names.sort()

    checking_sorting(original_list_country_names, sorted_list_country_names, i)

    #driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=CA")

    driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=CA'][title='Edit']").click()

    element_2 = driver.find_elements_by_css_selector('#table-zones > tbody > tr:not([class])')

    original_list_zones_ca = []

    sorted_list_zones_ca = []

    length_of_elements = len(element_2) - 2

    loop_for_zones_edit(element_2, original_list_zones_ca, sorted_list_zones_ca, length_of_elements)

    sorted_list_zones_ca.sort()

    checking_sorting(original_list_zones_ca, sorted_list_zones_ca, i)

    #driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US")

    driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US'][title='Edit']").click()

    element_3 = driver.find_elements_by_css_selector('#table-zones > tbody > tr:not([class])')

    original_list_zones_us = []

    sorted_list_zones_us = []

    length_of_elements_2 = len(element_3) - 2

    loop_for_zones_edit(element_3, original_list_zones_us, sorted_list_zones_us, length_of_elements_2)

    sorted_list_zones_us.sort()

    checking_sorting(original_list_zones_us, sorted_list_zones_us, i)


def test_check_sort2(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    # driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=1")

    driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=1'][title='Edit']").click()

    el3 = driver.find_elements_by_css_selector(".dataTable tr select[name*='[zone_code]'] option[selected='selected']")
    list3 = []
    sorted_list3 = []

    loop_for_zones(el3, list3, sorted_list3)

    sorted_list3.sort()

    checking_sorting(list3, sorted_list3)

    #driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=2")

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=2'][title='Edit']").click()

    el4 = driver.find_elements_by_css_selector(".dataTable tr select[name*='[zone_code]'] option[selected='selected']")
    list4 = []
    sorted_list4 = []

    loop_for_zones(el4, list4, sorted_list4)

    sorted_list4.sort()

    checking_sorting(list4, sorted_list4)
