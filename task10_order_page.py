import pytest
from selenium import webdriver
import re


@pytest.fixture
def driver_chrome(request):
    # создание драйвера. Инициализация браузера
    wd = webdriver.Chrome()
    # wd = webdriver.Chrome("D:/python_selenium_test/chromedriver_win32/chromedriver.exe")
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def driver_ie(request):
    # создание драйвера. Инициализация браузера
    wd = webdriver.Ie()
    # wd = webdriver.Chrome("D:/python_selenium_test/chromedriver_win32/chromedriver.exe")
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def driver_firefox(request):
    # создание драйвера. Инициализация браузера
    wd = webdriver.Firefox()
    # wd = webdriver.Chrome("D:/python_selenium_test/chromedriver_win32/chromedriver.exe")
    request.addfinalizer(wd.quit)
    return wd


def get_rgb(str_rgb):
    # Получаем из строки отдельные записи значений элементов R, G, B

    color_list = re.findall(r'\d+', str_rgb)

    r = color_list[0]
    g = color_list[1]
    b = color_list[2]

    return [r, g, b]


def compare_element(element_1, element_2):
    if element_1 == element_2:
        print('Elements expected \n')
    else:
        print('Elements not expected \n')


def check_regular_price_chrome(colors, line):
    exp_color_rgb_1 = '119'

    exp_color_rgb_2 = '102'

    exp_line = 'line-through'

    if (((colors[0] and colors[1] and colors[2]) == exp_color_rgb_1) or
            ((colors[0] and colors[1] and colors[2]) == exp_color_rgb_2) and (line == exp_line)):

        print('Expected element properties \n')
    else:
        print('Not expected element properties \n')


def check_discount_price_chrome(colors, font):
    exp_color_gb = '0'

    exp_font = '700'

    if (colors[1] and (colors[2]) == exp_color_gb) and (font == exp_font):

        print('Expected element properties \n')
    else:
        print('Not expected element properties \n')


def check_regular_price_firefox(colors, line):
    exp_color_rgb_1 = '119'

    exp_color_rgb_2 = '102'

    exp_line = 'line-through'

    if (((colors[0] and colors[1] and colors[2]) == exp_color_rgb_1) or
            ((colors[0] and colors[1] and colors[2]) == exp_color_rgb_2) and (line == exp_line)):

        print('Expected element properties in Firefox \n')
    else:
        print('Not expected element properties in Firefox \n')


def check_regular_price_ie(colors, line):
    exp_color_rgb_1 = '119'

    exp_color_rgb_2 = '102'

    exp_line = ''

    if (((colors[0] and colors[1] and colors[2]) == exp_color_rgb_1) or
            ((colors[0] and colors[1] and colors[2]) == exp_color_rgb_2) and (line == exp_line)):
        print('Expected element properties in IE \n')
    else:
        print('Not expected element properties in IE \n')


def check_discount_price_ie(colors, font):
    exp_color_gb = '0'

    exp_font = '700'

    exp_font2 = '900'

    if (colors[1] and (colors[2]) == exp_color_gb) and ((font == exp_font) or (font == exp_font2)):

        print('Expected element properties in IE \n')
    else:
        print('Not expected element properties in IE \n')


def check_discount_price_firefox(colors, font):
    exp_color_gb = '0'

    exp_font = '700'

    exp_font2 = '900'

    if (colors[1] and (colors[2]) == exp_color_gb) and ((font == exp_font) or (font == exp_font2)):

        print('Expected element properties in Firefox \n')
    else:
        print('Not expected element properties in Firefox \n')


def test_check_orders(driver_chrome):
    # test_login(driver)

    ### Атрибуты главной страницы

    driver_chrome.get("http://localhost/litecart/en/")

    # Название
    main_duck_name = driver_chrome.find_element_by_css_selector("div#box-campaigns div.name").get_attribute(
        "textContent")

    # Обычная цена
    main_duck_price = driver_chrome.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").get_attribute("textContent")

    # Скидочная цена
    main_duck_price_discount = driver_chrome.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").get_attribute("textContent")

    # Цвета
    m_color_price = driver_chrome.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("color")

    m_color_price_discount = driver_chrome.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    m_price_line = driver_chrome.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("text-decoration-line")

    # Шрифт
    m_bold = driver_chrome.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-weight")

    # Обычная
    main_size = driver_chrome.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("font-size")

    # Скидочная
    main_size_discount = driver_chrome.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-size")

    ### Атрибуты открытой ссылки

    driver_chrome.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")

    # Название
    duck_name = driver_chrome.find_element_by_css_selector("h1.title").get_attribute("textContent")

    # Обычная цена
    duck_price = driver_chrome.find_element_by_css_selector("div.information s.regular-price").get_attribute(
        "textContent")

    # Скидочная цена
    duck_price_discount = driver_chrome.find_element_by_css_selector(
        "div.information strong.campaign-price").get_attribute("textContent")

    # Цвета
    color_price = driver_chrome.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "color")

    color_price_discount = driver_chrome.find_element_by_css_selector(
        "div.information strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    price_line = driver_chrome.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "text-decoration-line")

    # Шрифт
    sub_bold = driver_chrome.find_element_by_css_selector(
        "div.information strong.campaign-price").value_of_css_property("font-weight")

    # Размер

    # Обычная цена
    duck_size = driver_chrome.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "font-size")

    # Скидочная цена
    duck_size_discount = driver_chrome.find_element_by_css_selector(
        "div.information strong.campaign-price").value_of_css_property("font-size")

    # Сравнения названий

    compare_element(main_duck_name, duck_name)

    compare_element(main_duck_price, duck_price)

    compare_element(main_duck_price_discount, duck_price_discount)

    # Соответствие зачернутости и цвету

    check_regular_price_chrome(get_rgb(m_color_price), m_price_line)

    check_regular_price_chrome(get_rgb(color_price), price_line)

    # Соответствие стилю и цвету

    check_discount_price_chrome(get_rgb(m_color_price_discount), m_bold)

    check_discount_price_chrome(get_rgb(color_price_discount), sub_bold)

    # Сравнение размера

    compare_element(main_size, main_size_discount)

    compare_element(duck_size, duck_size_discount)

    print("----------------------------------------- Test Chrome Done ----------------------------------------- \n")


def test_check_orders_ff(driver_firefox):
    # test_login(driver)

    ### Атрибуты главной страницы

    driver_firefox.get("http://localhost/litecart/en/")

    # Название

    main_duck_name = driver_firefox.find_element_by_css_selector("div#box-campaigns div.name").get_attribute(
        "textContent")

    # Обычная цена
    main_duck_price = driver_firefox.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").get_attribute("textContent")

    # Скидочная цена
    main_duck_price_discount = driver_firefox.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").get_attribute("textContent")

    # Цвета
    m_color_price = driver_firefox.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("color")

    m_color_price_discount = driver_firefox.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    m_price_line = driver_firefox.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("text-decoration-line")

    # Шрифт
    m_bold = driver_firefox.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-weight")

    # Обычная
    main_size = driver_firefox.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("font-size")

    # Скидочная
    main_size_discount = driver_firefox.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-size")

    ### Атрибуты открытой ссылки

    driver_firefox.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")

    # Название
    duck_name = driver_firefox.find_element_by_css_selector("h1.title").get_attribute("textContent")

    # Обычная цена
    duck_price = driver_firefox.find_element_by_css_selector("div.information s.regular-price").get_attribute(
        "textContent")

    # Скидочная цена
    duck_price_discount = driver_firefox.find_element_by_css_selector(
        "div.information strong.campaign-price").get_attribute("textContent")

    # Цвета
    color_price = driver_firefox.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "color")

    color_price_discount = driver_firefox.find_element_by_css_selector(
        "div.information strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    price_line = driver_firefox.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "text-decoration-line")

    # Шрифт?
    sub_bold = driver_firefox.find_element_by_css_selector(
        "div.information strong.campaign-price").value_of_css_property("font-weight")

    # Размер

    # Обычная цена
    duck_size = driver_firefox.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "font-size")

    # Скидочная цена
    duck_size_discount = driver_firefox.find_element_by_css_selector(
        "div.information strong.campaign-price").value_of_css_property("font-size")

    # Сравнения названий

    compare_element(main_duck_name, duck_name)

    compare_element(main_duck_price, duck_price)

    compare_element(main_duck_price_discount, duck_price_discount)

    # Соответствие зачернутости и цвету

    check_regular_price_firefox(get_rgb(m_color_price), m_price_line)

    check_regular_price_firefox(get_rgb(color_price), price_line)

    # Соответствие стилю и цвету

    check_discount_price_firefox(get_rgb(m_color_price_discount), m_bold)

    check_discount_price_firefox(get_rgb(color_price_discount), sub_bold)

    # Сравнение размера

    compare_element(main_size, main_size_discount)

    compare_element(duck_size, duck_size_discount)

    print("----------------------------------------- Test Firefox Done ----------------------------------------- \n")


def test_check_orders_ie(driver_ie):
    # test_login(driver)

    ### Атрибуты главной страницы

    driver_ie.get("http://localhost/litecart/en/")

    # Название

    main_duck_name = driver_ie.find_element_by_css_selector("div#box-campaigns div.name").get_attribute("textContent")

    # Обычная цена
    main_duck_price = driver_ie.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").get_attribute("textContent")

    # Скидочная цена
    main_duck_price_discount = driver_ie.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").get_attribute("textContent")

    # Цвета
    m_color_price = driver_ie.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("color")

    m_color_price_discount = driver_ie.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    m_price_line = driver_ie.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("text-decoration-line")

    # Шрифт
    m_bold = driver_ie.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-weight")

    # Обычная
    main_size = driver_ie.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper s.regular-price").value_of_css_property("font-size")

    # Скидочная
    main_size_discount = driver_ie.find_element_by_css_selector(
        "div#box-campaigns div.price-wrapper strong.campaign-price").value_of_css_property("font-size")

    ### Атрибуты открытой ссылки

    driver_ie.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")

    # Название
    duck_name = driver_ie.find_element_by_css_selector("h1.title").get_attribute("textContent")

    # Обычная цена
    duck_price = driver_ie.find_element_by_css_selector("div.information s.regular-price").get_attribute("textContent")

    # Скидочная цена
    duck_price_discount = driver_ie.find_element_by_css_selector("div.information strong.campaign-price").get_attribute(
        "textContent")

    # Цвета
    color_price = driver_ie.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "color")

    color_price_discount = driver_ie.find_element_by_css_selector(
        "div.information strong.campaign-price").value_of_css_property("color")

    # Зачеркутость (line-through)
    price_line = driver_ie.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "text-decoration-line")

    # Шрифт?
    sub_bold = driver_ie.find_element_by_css_selector("div.information strong.campaign-price").value_of_css_property(
        "font-weight")

    # Размер

    # Обычная цена
    duck_size = driver_ie.find_element_by_css_selector("div.information s.regular-price").value_of_css_property(
        "font-size")

    # Скидочная цена
    duck_size_discount = driver_ie.find_element_by_css_selector(
        "div.information strong.campaign-price").value_of_css_property("font-size")

    # Сравнения названий

    compare_element(main_duck_name, duck_name)

    compare_element(main_duck_price, duck_price)

    compare_element(main_duck_price_discount, duck_price_discount)

    # Соответствие зачернутости и цвету

    check_regular_price_ie(get_rgb(m_color_price), m_price_line)

    check_regular_price_ie(get_rgb(color_price), price_line)

    # Соответствие стилю и цвету

    check_discount_price_ie(get_rgb(m_color_price_discount), m_bold)

    check_discount_price_ie(get_rgb(color_price_discount), sub_bold)

    # Сравнение размера

    compare_element(main_size, main_size_discount)

    compare_element(duck_size, duck_size_discount)

    print("----------------------------------------- Test IE Done ----------------------------------------- \n")
