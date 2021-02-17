from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CouponsPage:
    # Initialize Web Driver
    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    add_coupon_button = (By.CSS_SELECTOR, "#button_add_a_coupon")
    coupon_name_input = (By.CSS_SELECTOR, "input[placeholder='Required']")
    promo_input = (By.CSS_SELECTOR, "input[placeholder='optional']")
    day_input = (By.CSS_SELECTOR, "select[name='Day']")
    discount_input = (By.CSS_SELECTOR, "input[name='Percent']")
    create_coupon_link = (By.CSS_SELECTOR, "#button_create_coupon_link")
    save_button = (By.CSS_SELECTOR, "#button_save_changes")
    coupon_list = (By.CSS_SELECTOR, "select[name='record']")

    # Click Add Coupons Button
    def add_coupon(self):
        self.driver.find_element(*CouponsPage.add_coupon_button).click()

    # Input name of coupon
    def set_coupon_name(self, name):
        input_name = self.driver.find_element(*CouponsPage.coupon_name_input)
        input_name.send_keys(name)

    # Input promo code
    def set_promo(self, promo):
        promo_box = self.driver.find_element(*CouponsPage.promo_input)
        promo_box.send_keys(promo)

    # Input date of expiration
    def set_expiration(self, expiration):
        select_day = Select(self.driver.find_element(*CouponsPage.day_input))
        select_day.select_by_value(value=expiration)

    # Input Discount amount
    def set_discount(self, discount):
        discount_box = self.driver.find_element(*CouponsPage.discount_input)
        discount_box.clear()
        discount_box.send_keys(discount)

    # Click Create Coupon Button
    def create_coupon(self):
        self.driver.find_element(*CouponsPage.create_coupon_link).click()

    # Click Save button
    def save(self):
        self.driver.find_element(*CouponsPage.save_button).click()

    # Get list of all coupons
    def get_coupon_list(self):
        coupons = self.driver.find_element(*CouponsPage.coupon_list)
        return coupons.text
