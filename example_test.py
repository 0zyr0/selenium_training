import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    # создание драйвера
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    # 10-секундное ожидание
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    wait.until(EC.title_is("webdriver - Поиск в Google"))
