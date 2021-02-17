from TestData.HomePageData import HomePage
from utilities.BaseClass import BaseClass


# ------ Test Parameters ------
name = "Test-Coupon"
promo = "55556"
date = "27"
discount = "50"


class TestCouponCreation(BaseClass):

    # Verify that a coupon can be created from Back Office
    def test_coupon_creation(self):
        # Get Logger
        log = self.getLogger()
        log.info("TEST HAS STARTED")

        # Set the driver to ShopSite HomePage
        home_page = HomePage(self.driver)

        # Navigate to Merchandising
        merchandising = home_page.get_merchandising_page()

        # Navigate to Coupons
        coupon_page = merchandising.get_coupon_page()

        # Click Add Coupon
        coupon_page.add_coupon()

        # Fill Coupon Display Name
        coupon_page.set_coupon_name(name)

        # Enter Promo Code
        coupon_page.set_promo(promo)

        # Set Expiration Date
        coupon_page.set_expiration(date)

        # Set Discount
        coupon_page.set_discount(discount)

        # Click Create Coupon Link
        coupon_page.create_coupon()

        # Save Changes
        coupon_page.save()

        # Verify that Coupon is in coupon_list
        assert name in coupon_page.get_coupon_list()
