import time
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    add_product_button = (By.CSS_SELECTOR, "#add_product")
    product_name_input = (By.CSS_SELECTOR, "input[name='-1:0']")
    product_price_input = (By.CSS_SELECTOR, "input[name='-1:1']")
    save_page_button = (By.CSS_SELECTOR, "input[value='Save']")
    product_list = (By.CSS_SELECTOR, "table[id='fixed_products']")

    # Click Add Product button
    def add_product(self):
        time.sleep(1)
        self.driver.find_element(*ProductPage.add_product_button).click()

    # Input Name of the product
    def set_name(self, name):
        self.driver.find_element(*ProductPage.product_name_input).send_keys(name)

    # Input Price of the product
    def set_price(self, price):
        x = self.driver.find_element(*ProductPage.product_price_input)
        x.clear()
        x.send_keys(price)

    # Click Save button
    def save(self):
        self.driver.find_element(*ProductPage.save_page_button).click()

    # Get list of all products
    def get_product_list(self):
        products = self.driver.find_element(*ProductPage.product_list)
        return products.text

