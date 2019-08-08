from selenium import webdriver
from Task19.pages.admin_login_page import AdminLoginPage
from Task19.pages.main_page import MainPage
from Task19.pages.checkout_page import CheckoutPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.admin_login_page = AdminLoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_order(self):
        self.main_page.open()
        self.main_page.select_order()

    def delete_order(self):
        self.checkout_page.open()
        self.checkout_page.delete_order()

