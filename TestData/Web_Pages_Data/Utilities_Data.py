from selenium.webdriver.common.by import By
from TestData.Database_Data import DatabasePage


class UtilitiesPage:

    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    option_database = (By.CSS_SELECTOR, "#button_database")

    # Click on the Database Tab of Utilities
    def get_database_page(self):
        self.driver.find_element(*UtilitiesPage.option_database).click()
        manage_database = DatabasePage(self.driver)
        return manage_database
