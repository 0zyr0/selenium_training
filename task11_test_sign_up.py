import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import random
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


def generate_email(user, out="account"):
    cache = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] * 10
    random.shuffle(cache)
    buf = ""
    for i in range(0, 10):
        buf += str(cache.pop())

    user.email = "test" + buf + "@mail.org"

    with open(out, "a") as file:
        file.write(user.email + "\n")
        file.close()

def data_for_test():
    first_name = 'test'
    last_name = 'test'
    postcode = '12345'
    phone = '+1'
    password = 'test'
    conf_password = 'test'
    adress_1 = 'test'
    adress_2 = 'test'
    city = 'City-17'

    #email = generate_mail()


def test_check_stickers(driver):



    print(generate_email(1, 2))

    driver.get("http://localhost/litecart/en/")

    driver.find_element_by_link_text("New customers click here").click()

    print('Sign up test done')


def test_check_email(driver):
    test_login(driver)

    driver.get("http://localhost/litecart/admin/")

    elements = driver.find_elements_by_css_selector("li#app-")

    driver.find_elements_by_id("app-")[4].click()

    customers = driver.find_elements_by_css_selector("tr.row")

    email_list = []

    for i, customer in enumerate(customers):

        driver.find_elements_by_css_selector("tr.row td a i")[i].click()

        verify_email = driver.find_element_by_name("email").get_attribute('value')

        email_list.append(verify_email)

        driver.find_element_by_name("cancel").click()

    return email_list


# def check_mail(atr):
#     email_list = test_check_email(driver)
#     if atr in email_list:
#         print('This email adress not available!')
#     else:
#         atr = ge

# Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart (не в админке, а в клиентской части магазина).
#
# Сценарий должен состоять из следующих частей:
#
# 1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты (чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария),
# 2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
# 3) повторный вход в только что созданную учётную запись,
# 4) и ещё раз выход.
#
#     В качестве страны выбирайте United States, штат произвольный. При этом формат индекса -- пять цифр.
#
#     Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
#
#     Проверки можно никакие не делать, только действия -- заполнение полей, нажатия на кнопки и ссылки. Если сценарий дошёл до конца, то есть созданный пользователь смог выполнить вход и выход -- значит создание прошло успешно.