import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    # создание драйвера. Инициализация браузера
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(10)
    #wait.until(EC.title_is("My Store"))

def test_left_frame_click(driver):
    test_login(driver)

    # Appearence
    driver.find_element_by_css_selector("li#app-").click()
    assert "Template" in driver.title
    driver.find_element_by_css_selector("li#doc-logotype").click()
    assert "Logotype" in driver.title

    # Catalog
    #driver.find_element_by_css_selector("li:nth-child(2)").click()

    driver.find_elements_by_id("app-")[1].click()
    assert "Catalog" in driver.title
    driver.find_element_by_css_selector("li#doc-product_groups").click()
    assert "Product Groups" in driver.title
    driver.find_element_by_css_selector("li#doc-option_groups").click()
    assert "Option Groups" in driver.title
    driver.find_element_by_css_selector("li#doc-manufacturers").click()
    assert "Manufacturers" in driver.title
    driver.find_element_by_css_selector("li#doc-suppliers").click()
    assert "Suppliers" in driver.title
    driver.find_element_by_css_selector("li#doc-delivery_statuses").click()
    assert "Delivery Statuses" in driver.title
    driver.find_element_by_css_selector("li#doc-sold_out_statuses").click()
    assert "Sold Out Statuses" in driver.title
    driver.find_element_by_css_selector("li#doc-quantity_units").click()
    assert "Quantity Units" in driver.title
    driver.find_element_by_css_selector("li#doc-csv").click()
    assert "CSV Import/Export" in driver.title

    # Countries
    driver.find_elements_by_id("app-")[2].click()
    assert "Countries" in driver.title

    # Currencies
    driver.find_elements_by_id("app-")[3].click()
    assert "Currencies" in driver.title

    # Customers
    driver.find_elements_by_id("app-")[4].click()
    assert "Customers" in driver.title
    driver.find_element_by_css_selector("li#doc-csv").click()
    assert "CSV Import/Export" in driver.title
    driver.find_element_by_css_selector("li#doc-newsletter").click()
    assert "Newsletter" in driver.title

    # Geo Zones
    driver.find_elements_by_id("app-")[5].click()
    assert "Geo Zones" in driver.title

    # Languages
    driver.find_elements_by_id("app-")[6].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-storage_encoding").click()
    assert "Storage Encoding" in driver.title

    # Job Modules
    driver.find_elements_by_id("app-")[7].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-customer").click()
    assert "Customer Modules" in driver.title
    driver.find_element_by_css_selector("li#doc-shipping").click()
    assert "Shipping Modules" in driver.title
    driver.find_element_by_css_selector("li#doc-payment").click()
    assert "Payment Modules" in driver.title
    driver.find_element_by_css_selector("li#doc-order_total").click()
    assert "Order Total Modules" in driver.title
    driver.find_element_by_css_selector("li#doc-order_success").click()
    assert "Order Success Modules" in driver.title
    driver.find_element_by_css_selector("li#doc-order_action").click()
    assert "Order Action Modules" in driver.title

    # Job Modules
    driver.find_elements_by_id("app-")[8].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-storage_encoding").click()
    assert "Storage Encoding" in driver.title

    # Orders
    driver.find_elements_by_id("app-")[9].click()
    assert "Orders" in driver.title
    driver.find_element_by_css_selector("li#doc-order_statuses").click()
    assert "Order Statuses" in driver.title

    # Pages
    driver.find_elements_by_id("app-")[10].click()
    assert "Pages" in driver.title

    # Job Modules
    driver.find_elements_by_id("app-")[11].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-storage_encoding").click()
    assert "Storage Encoding" in driver.title

    # Job Modules
    driver.find_elements_by_id("app-")[12].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-storage_encoding").click()
    assert "Storage Encoding" in driver.title

    # Job Modules
    driver.find_elements_by_id("app-")[13].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-storage_encoding").click()
    assert "Storage Encoding" in driver.title

    # Job Modules
    driver.find_elements_by_id("app-")[14].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-storage_encoding").click()
    assert "Storage Encoding" in driver.title

    # Job Modules
    driver.find_elements_by_id("app-")[15].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-storage_encoding").click()
    assert "Storage Encoding" in driver.title

    # Job Modules
    driver.find_elements_by_id("app-")[16].click()
    assert "Languages" in driver.title
    driver.find_element_by_css_selector("li#doc-storage_encoding").click()
    assert "Storage Encoding" in driver.title

    # настройка неявных ожиданий
    driver.implicitly_wait(10)


