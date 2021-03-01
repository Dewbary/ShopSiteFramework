from selenium.webdriver.common.by import By

from TestData.Commerce_Data import CommercePage
from TestData.Help_Data import HelpPage
from TestData.Images_Data import ImagesPage
from TestData.Merchandising_Data import MerchandisingPage
from TestData.Orders_Data import OrdersPage
from TestData.PagesData import Pages
from TestData.Preferences_Data import PreferencesPage
from TestData.Products_Data import ProductPage
from TestData.Reports_Data import ReportsPage
from TestData.Store_Data import StorePage
from TestData.Utilities_Data import UtilitiesPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    # All menu options
    menu_option_pages = (By.CSS_SELECTOR, "div[id='nav_icon_m1']")
    menu_option_products = (By.CSS_SELECTOR, "div[id='nav_icon_m2']")
    menu_option_images = (By.CSS_SELECTOR, "div[id='nav_icon_m3']")
    menu_option_merchandising = (By.CSS_SELECTOR, "div[id='nav_icon_m4']")
    menu_option_orders = (By.CSS_SELECTOR, "div[id='nav_icon_m5']")
    menu_option_reports = (By.CSS_SELECTOR, "div[id='nav_icon_m6']")
    menu_option_commerce = (By.CSS_SELECTOR, "div[id='nav_icon_m7']")
    menu_option_utilities = (By.CSS_SELECTOR, "div[id='nav_icon_m8']")
    menu_option_preferences = (By.CSS_SELECTOR, "div[id='nav_icon_m9']")
    menu_option_help = (By.CSS_SELECTOR, "div[id='nav_icon_m10']")

    # Navigate to Pages
    def get_pages(self):
        self.driver.find_element(*HomePage.menu_option_pages).click()  # * unpacks the tuple: menu_option_pages
        manage_pages_page = Pages(self.driver)
        return manage_pages_page

    # Navigate to Products
    def get_products_page(self):
        self.driver.find_element(*HomePage.menu_option_products).click()
        manage_products = ProductPage(self.driver)
        return manage_products

    # Navigate to Images
    def get_images_page(self):
        self.driver.find_element(*HomePage.menu_option_images).click()
        manage_images = ImagesPage(self.driver)
        return manage_images

    # Navigate to Merchandising
    def get_merchandising_page(self):
        self.driver.find_element(*HomePage.menu_option_merchandising).click()
        manage_merchandising = MerchandisingPage(self.driver)
        return manage_merchandising

    # Navigate to Orders
    def get_orders_page(self):
        self.driver.find_element(*HomePage.menu_option_orders).click()
        manage_orders = OrdersPage(self.driver)
        return manage_orders

    # Navigate to Reports
    def get_reports_page(self):
        self.driver.find_element(*HomePage.menu_option_reports).click()
        manage_reports = ReportsPage(self.driver)
        return manage_reports

    # Navigate to Commerce
    def get_commerce_page(self):
        self.driver.find_element(*HomePage.menu_option_commerce).click()
        manage_commerce = CommercePage(self.driver)
        return manage_commerce

    # Navigate to Utilities
    def get_utilities_page(self):
        self.driver.find_element(*HomePage.menu_option_utilities).click()
        manage_utilities = UtilitiesPage(self.driver)
        return manage_utilities

    # Navigate to Preferences
    def get_preferences_page(self):
        self.driver.find_element(*HomePage.menu_option_preferences).click()
        manage_preferences = PreferencesPage(self.driver)
        return manage_preferences

    # Navigate to Help
    def get_help_page(self):
        self.driver.find_element(*HomePage.menu_option_help).click()
        manage_help = HelpPage(self.driver)
        return manage_help

    # Navigate to Store's Main Page
    def get_store_page(self):
        self.driver.get("http://brendanqa.com/brendan/index.html")
        manage_store_page = StorePage(self.driver)
        return manage_store_page
