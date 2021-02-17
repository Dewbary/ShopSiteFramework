from TestData.HomePageData import HomePage
from utilities.BaseClass import BaseClass

# ------- Test Parameters -------
name = "Test Product Name"
price = "10"


class TestProductCreation(BaseClass):

    # Verify if a new product can be created
    def test_product_creation(self):
        # Get Logger
        log = self.getLogger()
        log.info("TEST HAS STARTED")

        # Set the driver to ShopSite HomePage
        home_page = HomePage(self.driver)

        # Set the driver to ProductPage
        manage_products = home_page.get_products_page()

        # Click Add Product
        manage_products.add_product()

        # Fill Product name and price boxes
        manage_products.set_name(name)
        manage_products.set_price(price)

        # Click Save
        manage_products.save()

        # Verify product in product_list
        assert name in manage_products.get_product_list()









