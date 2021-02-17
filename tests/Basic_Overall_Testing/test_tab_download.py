from TestData.HomePageData import HomePage
from utilities.BaseClass import BaseClass
import time

# ------- Test Parameters -------
fields = ['products', 'pages']
out_format = 'tab'
version = 'version 14.0'


class TestTabDownload(BaseClass):

    # Verify that tab-delimited files can be downloaded from the Back Office
    def test_tab_download(self):
        # Get Logger
        log = self.getLogger()
        log.info("TEST HAS STARTED")

        # Set the driver to ShopSite HomePage
        home_page = HomePage(self.driver)

        # Navigate to Utilities
        utilities_page = home_page.get_utilities_page()

        # Click Database
        database_page = utilities_page.get_database_page()

        # Click Download
        database_page.download()

        # Loop through products and pages databases
        for i in fields:
            # Select field
            database_page.set_table(i)

            # Click Download
            database_page.download()

            # Select Tab-Delimited text format
            database_page.set_format(out_format)

            # Set Version #
            database_page.set_version(version)

            # Click Proceed
            database_page.proceed()

            # Click Return (double-click)       **Check later if this could be a bug that we have to click submit twice
            database_page.click_return()
            time.sleep(1)
            database_page.click_return()
            time.sleep(1)

            # Verify that file has been downloaded
            database_page.verify_file_download()
