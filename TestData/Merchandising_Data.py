from selenium.webdriver.common.by import By
from TestData.Coupons_Data import CouponsPage


class MerchandisingPage:
    # Initialize Web Driver
    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    option_coupons = (By.CSS_SELECTOR, "#button_coupons")

    # Navigate to Coupon tab in Merchandising
    def get_coupon_page(self):
        self.driver.find_element(*MerchandisingPage.option_coupons).click()
        manage_coupons = CouponsPage(self.driver)
        return manage_coupons
