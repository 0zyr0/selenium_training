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


# def check_sort_elements():


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

    # --------------

    original_list_zones = []

    sorted_list_zones = []

    driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=CA")

    # elements = driver.find_elements_by_css_selector("table tbody tr:not([class])")

    #elements = driver.find_elements_by_css_selector("table tbody tr:not([class]) td[style*=text]")

    elements = driver.find_element_by_css_selector('#table-zones > tbody > tr')
    print(elements)
    array1 = []
    lengthOfElements = len(elements) - 1

    for i, el in enumerate(elements):
        array1.append(el.text)
        if i == lengthOfElements:
            break

        # original_list_country_names.append(re.match(r'^\d+\s*\w{2}\s*(.+)\d+$', element.text)[1].strip())
        # print(element.text)
        # original_list_country_names.append(re.match(r'^\d+\s*\w{2}\s*(.+)\d+$', element.text)[1].strip())
        #
        # sorted_list_country_names.append(re.match(r'^\d+\s*\w{2}\s*(.+)\d+$', element.text)[1].strip())

    print(array1)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US")

    # driver.find_element_by_css_selector("tr.row:nth-child(39) td:nth-child(5)").click()

    # driver.find_element_by_tag_name("tr.row:nth-child(224) td:nth-child(5)").click()

    print('Test Sort Country names has done')


def test_check_sort2(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=1")

    #driver.find_elements_by_css_selector(".dataTable tr select[name*='[zone_code]']")

    el3 = driver.find_elements_by_css_selector(".dataTable tr select[name*='[zone_code]'] option[selected='selected']")
    list3 = []
    sorted_list3 = []

    for i, element3 in enumerate(el3):
        list3.append(element3.get_property('text'))

    print(list3)

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

    print(list4)

    if list4[i] == sorted_list4[i]:
        print('Zones sorted by Aa..Zz', '\n')
    else:
        print(list4[i], ' not equals ', sorted_list4[i], '\n')
