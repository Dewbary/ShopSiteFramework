import time
from selenium.webdriver.common.by import By

class InputBox:

    def __init__(self, driver):
        self.driver = driver

    # //------------------------ Selectors ---------------------------//
    edit_page_content = (By.XPATH, "//input[@id='button_edit_page_content']")
    save_button = (By.XPATH, "//input[@id='button_save']")
    # //--------------------------------------------------------------//

    # Find all text input boxes and fill them with '1'
    def fill_text(self):
        # Store all input selectors found on the page
        input_selectors = self.driver.find_elements_by_css_selector("input[type='text']")
        # Iterate through each input selector in the list
        for i in input_selectors:
            try:
                i.clear()
                i.send_keys("1")
                print(i.get_attribute("class"))
            except:
                print("Input Error")
            finally:
                continue

    # Find all textarea boxes and fill them with '1'
    def fill_editor(self):
        # Find all textarea boxes and put them in a list
        input_selectors = self.driver.find_elements_by_css_selector("textarea")
        # iterate through each input selector
        for i in input_selectors:
            try:
                i.clear()
                i.send_keys("1")
            except:
                print("Input Error")
            finally:
                continue

    # Fills all input and textarea boxes
    def fill_all(self):
        # self.driver.get("")
        self.fill_text()
        self.fill_editor()

    # Saves changes
    def save(self):
        try:
            self.driver.find_element(*InputBox.save_button).click()
        except:
            print("There is no save button")

    # Verifies that changes have been implemented successfully
    def verify(self):
        pass

