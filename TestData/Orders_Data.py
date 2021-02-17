from selenium.webdriver.common.by import By


class OrdersPage:

    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    order_list = (By.CSS_SELECTOR, "select[id='ordernum']")

