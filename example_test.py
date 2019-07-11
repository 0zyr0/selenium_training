import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    # создание драйвера. Инициализация браузера
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    # 10-секундное ожидание
    wait = WebDriverWait(driver, 15)
    driver.find_element_by_class_name("MiYK0e").click()
    WebDriverWait(driver, 15)
    driver.find_element_by_id("K32").click()
    driver.find_element_by_class_name("MiYK0e").click()
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.refresh()
    driver.find_element_by_name("btnK").click()
    wait.until(EC.title_is("webdriver - Поиск в Google"))
