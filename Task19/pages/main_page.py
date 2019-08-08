from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://litecart.stqa.ru/en/")
        return self

    def select_order(self):
        for i in range(4):

            self.driver.find_element_by_tag_name("div[class='image-wrapper'] img.image:nth-child(1)").click()

            try:
                select_size = self.driver.find_element_by_css_selector("select[name='options[Size]']")

                Select(select_size).select_by_value("Small")

            except NoSuchElementException:
                True

            self.driver.find_element_by_name("add_cart_product").click()

            self.wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "span[class='quantity']"), str(i)))

            self.driver.find_element_by_tag_name("i[class='fa fa-home']").click()
