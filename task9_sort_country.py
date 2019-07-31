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

    sorted_list_country_names.sort()

    if original_list_country_names[i] == sorted_list_country_names[i]:
        print('Countries sorted by Aa..Zz', '\n')
    else:
        print(original_list_country_names[i], ' not equals ', sorted_list_country_names[i], '\n')

    # Canada Zones

    driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=CA")

    element_2 = driver.find_elements_by_css_selector('#table-zones > tbody > tr:not([class])')

    original_list_zones_ca = []

    sorted_list_zones_ca = []

    length_of_elements = len(element_2) - 2

    for i, el in enumerate(element_2):

        original_list_zones_ca.append(re.match(r'^\d+\s+\w{2}\s*(.*)$', el.text)[1].strip())

        sorted_list_zones_ca.append(re.match(r'^\d+\s+\w{2}\s*(.*)$', el.text)[1].strip())

        if i == length_of_elements:
            break

    sorted_list_zones_ca.sort()

    if original_list_zones_ca[i] == sorted_list_zones_ca[i]:
        print('Zones CA sorted by Aa..Zz', '\n')
    else:
        print(original_list_zones_ca[i], ' not equals ', sorted_list_zones_ca[i], '\n')

    # USA Zones

    driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US")

    element_3 = driver.find_elements_by_css_selector('#table-zones > tbody > tr:not([class])')

    original_list_zones_us = []

    sorted_list_zones_us = []

    length_of_elements_2 = len(element_3) - 2

    for i, el_us in enumerate(element_3):

        original_list_zones_us.append(re.match(r'^\d+\s+\w{2}\s*(.*)$', el_us.text)[1].strip())

        sorted_list_zones_us.append(re.match(r'^\d+\s+\w{2}\s*(.*)$', el_us.text)[1].strip())

        if i == length_of_elements_2:
            break

    sorted_list_zones_us.sort()

    if original_list_zones_us[i] == sorted_list_zones_us[i]:
        print('Zones US sorted by Aa..Zz', '\n')
    else:
        print(original_list_zones_us[i], ' not equals ', sorted_list_zones_us[i], '\n')

    print('*** Test Sort Country and Zones(Edit) names has done *** ')


def test_check_sort2(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=1")

    el3 = driver.find_elements_by_css_selector(".dataTable tr select[name*='[zone_code]'] option[selected='selected']")
    list3 = []
    sorted_list3 = []

    for i, element3 in enumerate(el3):

        list3.append(element3.get_property('text'))

        sorted_list3.append(element3.get_property('text'))

    sorted_list3.sort()

    if list3[i] == sorted_list3[i]:
        print('Zones sorted by Aa..Zz', '\n')
    else:
        print(list3[i], ' not equals ', sorted_list3[i], '\n')

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=2")

    el4 = driver.find_elements_by_css_selector(".dataTable tr select[name*='[zone_code]'] option[selected='selected']")
    list4 = []
    sorted_list4 = []

    for i, element4 in enumerate(el4):

        list4.append(element4.get_property('text'))

        sorted_list4.append(element4.get_property('text'))

    sorted_list4.sort()

    if list4[i] == sorted_list4[i]:
        print('Zones sorted by Aa..Zz', '\n')
    else:
        print(list4[i], ' not equals ', sorted_list4[i], '\n')

    print('*** Test Sort Zones names has done ***')


# def test_check_sort3(driver):
#     test_login(driver)
#     driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
#
#     driver.find_elements_by_tag_name().click()
#
#     el3 = driver.find_elements_by_css_selector(".dataTable tr select[name*='[zone_code]'] option[selected='selected']")
#     list3 = []
#     sorted_list3 = []
#
#     for i, element3 in enumerate(el3):
#
#         list3.append(element3.get_property('text'))
#
#         sorted_list3.append(element3.get_property('text'))
#
#     sorted_list3.sort()
#
#     if list3[i] == sorted_list3[i]:
#         print('Zones sorted by Aa..Zz', '\n')
#     else:
#         print(list3[i], ' not equals ', sorted_list3[i], '\n')
#
#     driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=2")
#
#     el4 = driver.find_elements_by_css_selector(".dataTable tr select[name*='[zone_code]'] option[selected='selected']")
#     list4 = []
#     sorted_list4 = []
#
#     for i, element4 in enumerate(el4):
#
#         list4.append(element4.get_property('text'))
#
#         sorted_list4.append(element4.get_property('text'))
#
#     sorted_list4.sort()
#
#     if list4[i] == sorted_list4[i]:
#         print('Zones sorted by Aa..Zz', '\n')
#     else:
#         print(list4[i], ' not equals ', sorted_list4[i], '\n')
#
#     print('*** Test Sort Zones names has done ***')