from TestData.HomePageData import HomePage
from utilities.BaseClass import BaseClass

# ------- Test Parameters -------
filepath = '/Users/brendan/Documents/Photos/starship.jpg'


class TestImageUpload(BaseClass):

    # Verify images can be uploaded to Back Office
    def test_image_upload(self):
        # Get Logger
        log = self.getLogger()
        log.info("TEST HAS STARTED")

        # Set the driver to ShopSite HomePage
        home_page = HomePage(self.driver)

        # Navigate to Images
        images = home_page.get_images_page()

        # Click on Upload Images
        images.upload_images()

        # Click Choose File Button
        images.file_upload(filepath)

        # Click on Upload
        images.send()

        # Verify that Image file is in Images directory
        assert "starship.jpg" in images.get_image_list()
