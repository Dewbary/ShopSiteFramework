import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class StorePage:
    # Initialize Webdriver
    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    sign_in_button = (By.XPATH, "//span[@class='d-none d-lg-inline-block ml-1'][normalize-space()='Sign In']")
    email_input = (By.CSS_SELECTOR, "input[tabindex='1']")
    password_input = (By.CSS_SELECTOR, "input[tabindex='2']")
    submit_sign_in = (By.CSS_SELECTOR, "input[type='submit']")
    home_button = (By.CSS_SELECTOR, "a[href='http://brendanqa.com/brendan/index.html']")
    add_to_cart_button = (By.CSS_SELECTOR, "button[id='submitForm58']")
    view_cart_button = (By.CSS_SELECTOR, "a[class='btn btn-primary']")
    checkout_button = (By.XPATH, "//input[@value='Checkout']")
    input_purchase_order = (By.CSS_SELECTOR, "input[name='pay1']")
    submit_order_button = (By.CSS_SELECTOR, "input[data-id='Submit My Order']")

    # Billing Input Fields
    billing_email = (By.XPATH, "//input[@name='Email']")
    billing_first = (By.XPATH, "//input[@name='First']")
    billing_last = (By.XPATH, "//input[@name='Last']")
    billing_address = (By.XPATH, "//input[@name='Address']")
    billing_city = (By.XPATH, "//input[@name='City']")
    billing_state = (By.CSS_SELECTOR, "select[name='State']")
    billing_ZIP = (By.XPATH, "//input[@name='Zip']")
    billing_phone = (By.XPATH, "//input[@name='Phone']")
    shipping_same_as_billing = (By.XPATH, "//input[@name='usebilling']")

    # Verify Order in BackOffice
    order_number = (By.CSS_SELECTOR, "h3[class='class=']")
    menu_option_orders = (By.CSS_SELECTOR, "div[id='nav_icon_m5']")
    list_all_orders = (By.XPATH, "//input[@id='button_list_all']")
    order_list = (By.CSS_SELECTOR, "select[id='ordernum']")

    # Click Sign-in button to login to in-store Account
    def sign_in(self):
        self.driver.find_element(*StorePage.sign_in_button).click()

    # Input Username and Password credentials to login to in-store Account
    def input_credentials(self, email, password):
        self.driver.find_element(*StorePage.email_input).send_keys(email)
        self.driver.find_element(*StorePage.password_input).send_keys(password)
        self.driver.find_element(*StorePage.submit_sign_in).click()
        self.driver.find_element(*StorePage.home_button).click()

    # Return to Store HomePage
    def home(self):
        self.driver.find_element(*StorePage.home_button).click()

    # Add Product to Cart
    def add_to_cart(self):
        self.driver.find_element(*StorePage.add_to_cart_button).click()

    # Navigate to Shopping cart page
    def view_cart(self):
        self.driver.find_element(*StorePage.view_cart_button).click()

    # Click Checkout button
    def checkout(self):
        self.driver.find_element(*StorePage.checkout_button).click()

    # Fill in billing info with generic data
    def fill_generic_billing(self):
        # Find and assign all fields
        email = self.driver.find_element(*StorePage.billing_email)
        first = self.driver.find_element(*StorePage.billing_first)
        last = self.driver.find_element(*StorePage.billing_last)
        address = self.driver.find_element(*StorePage.billing_address)
        city = self.driver.find_element(*StorePage.billing_city)
        state = Select(self.driver.find_element(*StorePage.billing_state))
        ZIP = self.driver.find_element(*StorePage.billing_ZIP)
        phone = self.driver.find_element(*StorePage.billing_phone)
        same_as = self.driver.find_element(*StorePage.shipping_same_as_billing)
        purchase_order = self.driver.find_element(*StorePage.input_purchase_order)

        # Clear all input fields of pre-generated data
        email.clear()
        first.clear()
        last.clear()
        address.clear()
        city.clear()
        ZIP.clear()
        phone.clear()

        # Set all fields
        email.send_keys("brendandewberry99@gmail.com")
        first.send_keys("brendan")
        last.send_keys("dewberry")
        address.send_keys("1234 South")
        city.send_keys("Provo")
        state.select_by_value("AL")
        ZIP.send_keys("88888")
        phone.send_keys("4351111111")
        same_as.click()
        purchase_order.send_keys("1234")

    # Click Submit to send order through
    def submit_order(self):
        self.driver.find_element(*StorePage.submit_order_button).click()
        time.sleep(3)

    # Check if Order shows up in the Orders tab of Back Office
    def verify_order(self):
        order_num = self.driver.find_element(*StorePage.order_number).text
        order_num = order_num[-4:]
        print(order_num)
        time.sleep(2)
        self.driver.get("http://brendanqa.com/cgi-bin/brendan/ss/start.cgi")
        time.sleep(1)
        self.driver.find_element(*StorePage.menu_option_orders).click()
        time.sleep(1)
        self.driver.find_element(*StorePage.list_all_orders).click()
        orders = self.driver.find_element(*StorePage.order_list).text

        assert order_num in orders


