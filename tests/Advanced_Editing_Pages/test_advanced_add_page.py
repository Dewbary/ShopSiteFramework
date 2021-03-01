from TestData.HomePageData import HomePage
from utilities.BaseClass import BaseClass
from TestData.Inputbox_Data import InputBox

# ------- Test Parameters -------


# Verify that pages can be created
class TestAddPageAdvanced(BaseClass):

    def test_add_page_text(self):
        # Set the driver to ShopSite HomePage
        home_page = HomePage(self.driver)

        # Navigate to the Pages tab in navbar
        manage_pages_page = home_page.get_pages()

        # Click Add a Page
        manage_pages_page.add_page()

        # Fill all fields
        page_info = InputBox(self.driver)  # Pass the driver to the InputBox Class
        page_info.fill_all()



    # def test_add_page_images(self):
    #     pass
    #
    # def test_add_page_checkboxes(self):
    #     pass
    #
    # def test_add_page_numInput(self):
    #     pass
    #
    # def test_add_page_links(self):
    #     pass
    #
    # def test_add_page_templates(self):
    #     pass






