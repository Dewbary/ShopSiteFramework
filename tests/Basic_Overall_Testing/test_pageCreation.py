from TestData.HomePageData import HomePage
from utilities.BaseClass import BaseClass

# ------- Test Parameters -------
page_title = "Test Title"


# Verify that pages can be created
class TestCreatePage(BaseClass):

    def test_pageCreation(self):
        # Get Logger
        log = self.getLogger()
        log.info("TEST HAS STARTED")

        # Set the driver to ShopSite HomePage
        home_page = HomePage(self.driver)

        # Navigate to the Pages tab in navbar
        manage_pages_page = home_page.get_pages()

        # Navigate to create a new page screen
        edit_page = manage_pages_page.add_page()

        # Fill in Page information
        edit_page.fill_page_title(page_title)

        # Save Page
        edit_page.save()

        # Validate that the Page has been created
        assert page_title in edit_page.get_page_list()






