from TestData.HomePageData import HomePage
from TestData.Inputbox_Data import InputBox
from utilities.BaseClass import BaseClass

# ------- Test Parameters -------
path = " "


# Verify that pages can be created
class TestText(BaseClass):

    def text_checker(self):
        # Grabs assigned page
        test_page = InputBox(self.driver)

        # Finds and fills all text boxes
        test_page.fill_all()

        # Save Changes
        test_page.save()

        # Verify changes are implemented
        test_page.verify()