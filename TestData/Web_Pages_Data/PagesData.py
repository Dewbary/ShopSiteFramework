from selenium.webdriver.common.by import By


class Pages:
    # Initialize Web Driver
    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    add_page_button = (By.CSS_SELECTOR, "input[value='Add a Page']")
    page_title_input = (By.CSS_SELECTOR, "input[name='-1:0']")
    save_page_button = (By.CSS_SELECTOR, "input[value='Save']")
    page_list = (By.CSS_SELECTOR, "select[id='recs']")

    # Click Add new page button
    def add_page(self):
        self.driver.find_element(*Pages.add_page_button).click()
        edit_page = Pages(self.driver)
        return edit_page

    # Input Title name of the page to be created
    def fill_page_title(self, title):
        return self.driver.find_element(*Pages.page_title_input).send_keys(title)

    # Click the Save button
    def save(self):
        self.driver.find_element(*Pages.save_page_button).click()

    # Get list of all pages
    def get_page_list(self):
        x = self.driver.find_element(*Pages.page_list)
        return x.text




