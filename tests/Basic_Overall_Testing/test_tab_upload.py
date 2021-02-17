from TestData.HomePageData import HomePage
from utilities.BaseClass import BaseClass


# ------- TEST PARAMETERS -------
fields = ['products', 'pages']
files = ['/products.txt', '/pages.txt']


class TestTabDownload(BaseClass):

    # Verify that tab-delimited file can be uploaded to the Back Office
    def test_tab_upload(self):
        # Get Logger
        log = self.getLogger()
        log.info("TEST HAS STARTED")

        # Set the driver to ShopSite HomePage
        home_page = HomePage(self.driver)

        # Navigate to Utilities
        utilities_page = home_page.get_utilities_page()

        # Click Database
        database_page = utilities_page.get_database_page()

        # Loop through Products and Pages fields
        for i in range(len(fields)):
            # Click Upload
            database_page.upload()

            # Select Products/Pages
            database_page.set_table(fields[i])

            # Click Upload
            database_page.upload()

            # Get tab-delimited file
            database_page.get_file(files[i])

            # Upload file
            database_page.upload_file()

            # Click Proceed
            database_page.proceed()

            # Click OK to return
            database_page.OK()

            # Verify that products/pages have been added
            # TODO: database_page.verify_upload()

