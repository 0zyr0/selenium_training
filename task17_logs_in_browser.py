import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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


def test_log_browser(driver):
    # enable browser logging
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=d)

    # driver = webdriver.Chrome(desired_capabilities=d, service_args=["--verbose", "--log-path=D:\\qc1.log"])

    test_login(driver)

    driver.get("http://localhost/litecart/admin/")

    driver.find_element_by_tag_name("li#app-:nth-child(2)").click()

    driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1']").click()

    elements = driver.find_elements_by_tag_name("i[class='fa fa-pencil']")

    for i, element in enumerate(elements):
        driver.find_elements_by_tag_name("i[class='fa fa-pencil']")[i].click()

        #driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()

        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")

        print("\n", driver.get_log("browser"))

        driver.find_element_by_tag_name("a[href='http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1']").click()
