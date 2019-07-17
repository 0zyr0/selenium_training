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


def compare_element(element_1, element_2):

    if element_1 == element_2:
        print('Elements compared \n')
    else:
        print('Elements not compared \n')


def test_check_orders(driver):
    test_login(driver)

    # main_duck_list = []
    #
    # duck_list = []

        ### Атрибуты главной страницы

    driver.get("http://localhost/litecart/en/")

    # Название
    main_duck_name = driver.find_element_by_css_selector("div#box-campaigns div.name").get_attribute("textContent")

    # Обычная цена
    main_duck_price = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper s.regular-price").get_attribute("textContent")

    # Скидочная цена
    main_duck_price_discount = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper strong.campaign-price").get_attribute("textContent")

    # Цвета
    m_color_price = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("color")

    m_color_price_discount = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    m_price_line = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("text-decoration-line")

    # Шрифт
    m_bold = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-weight")

    # Обычная
    main_size = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("font-size")

    # Скидочная
    main_size_discount = driver.find_element_by_css_selector("div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-size")

    main_duck_list = list(main_duck_name, main_duck_price, main_duck_price_discount, m_color_price, m_color_price_discount, m_price_line, m_bold, main_size, main_size_discount)

    print('\n', main_duck_list, '\n')

        ### Атрибуты открытой ссылки

    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")

    # Название
    duck_name = driver.find_element_by_css_selector("h1.title").get_attribute("textContent")

    # Обычная цена
    duck_price = driver.find_element_by_css_selector("div.information s.regular-price").get_attribute("textContent")

    # Скидочная цена
    duck_price_discount = driver.find_element_by_css_selector("div.information strong.campaign-price").get_attribute("textContent")

    # Цвета
    color_price = driver.find_element_by_css_selector("div.information s.regular-price").value_of_css_property("color")

    color_price_discount = driver.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    price_line = driver.find_element_by_css_selector("div.information s.regular-price").value_of_css_property("text-decoration-line")

    # Шрифт?
    sub_bold = driver.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property("font-weight")

    # Размер

    # Обычная цена
    duck_size = driver.find_element_by_css_selector("div.information s.regular-price").value_of_css_property("font-size")

    # Скидочная цена
    duck_size_discount = driver.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property("font-size")

    # duck_list = list(duck_name, duck_price, duck_price_discount, color_price, color_price_discount, price_line, sub_bold, duck_size, duck_size_discount)
    #
    # print('\n', duck_list, '\n')


    #compare_element()


