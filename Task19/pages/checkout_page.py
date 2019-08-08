from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://litecart.stqa.ru/en/checkout")
        return self

    def delete_order(self):
        for i in range(4):
            self.driver.find_element_by_tag_name("button[value='Remove']").click()

            self.wait.until(EC.invisibility_of_element((By.TAG_NAME, "li[class='shortcut']")))
