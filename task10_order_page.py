import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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


def test_check_orders(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/en/")

    main_duck_name = driver.find_element_by_css_selector("div#box-campaigns div.name").get_attribute("textContent")

    # Обычная
    main_duck_price = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper s.regular-price").get_attribute("textContent")

    # Скидочная
    main_duck_price_discount = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper strong.campaign-price").get_attribute("textContent")

    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")

    duck_name = driver.find_element_by_css_selector("h1.title").get_attribute("textContent")

    # Обычная цена
    duck_price = driver.find_element_by_css_selector("div.information s.regular-price").get_attribute("textContent")

    # Скидочная цена
    duck_price_discount = driver.find_element_by_css_selector("div.information strong.campaign-price").get_attribute("textContent")


    # Цвета
    m_color_price = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("color")

    m_color_price_discount = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("color")

    color_price = driver.find_element_by_css_selector("div.information s.regular-price").value_of_css_property("color")

    color_price_discount = driver.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    m_price_line = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("text-decoration-line")

    price_line = driver.find_element_by_css_selector("div.information s.regular-price").value_of_css_property("text-decoration-line")

    # Шрифт?
    driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-weight")

    # в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
    # г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
    # (цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
    # д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)



