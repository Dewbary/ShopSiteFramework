from TestData.HomePageData import HomePage
from utilities.BaseClass import BaseClass


# -------- Test Parameters --------
email = 'brendandewberry99@gmail.com'
password = 'test1234'


class TestPlaceOrder(BaseClass):

    # Verify that products can be created
    def test_place_order(self):
        # Get Logger
        log = self.getLogger()
        log.info("TEST HAS STARTED")

        # Set the driver to ShopSite HomePage
        home_page = HomePage(self.driver)

        # Navigate to store home page
        store_page = home_page.get_store_page()

        # Sign in to the store
        store_page.sign_in()

        # Input email & password/Click sign in button
        store_page.input_credentials(email, password)

        # Navigate back to the Home Page
        store_page.home()

        # Locate test-product, and add it to cart
        store_page.add_to_cart()

        # Click on View Cart
        store_page.view_cart()

        # Click on Checkout twice
        store_page.checkout()

        # Fill in billing information
        store_page.fill_generic_billing()

        # Submit order
        store_page.submit_order()

        # Verify order in order_list in the Back Office
        store_page.verify_order()
