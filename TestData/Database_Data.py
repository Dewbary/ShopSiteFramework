import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DatabasePage:

    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    upload_button = (By.CSS_SELECTOR, "#button_upload")
    download_button = (By.CSS_SELECTOR, "#button_download")
    products_radio = (By.CSS_SELECTOR, "#table-products")
    pages_radio = (By.CSS_SELECTOR, "#table-pages")
    tab_format_radio = (By.CSS_SELECTOR, "input[value='tab_delim']")
    version_select = (By.CSS_SELECTOR, "select[id='tab_version']")
    proceed_button = (By.CSS_SELECTOR, "#button_proceed")
    return_button = (By.CSS_SELECTOR, "#button_return")
    file_button = (By.CSS_SELECTOR, "#Desktop")
    upload_file_button = (By.CSS_SELECTOR, "#button_upload_file")
    OK_button = (By.CSS_SELECTOR, "#button_ok")

    # Click Download button
    def download(self):
        self.driver.find_element(*DatabasePage.download_button).click()

    # Set the table options
    def set_table(self, field):
        if field == "products":
            self.driver.find_element(*DatabasePage.products_radio).click()
        elif field == "pages":
            self.driver.find_element(*DatabasePage.pages_radio).click()
        else:  # Error
            print("Invalid table field input")

    # Set format of file to upload/download
    def set_format(self, format):
        if format == 'tab':
            self.driver.find_element(*DatabasePage.tab_format_radio).click()
        else:  # Error
            print("Invalid radio input")

    # Set the file download version
    def set_version(self, version):
        select = Select(self.driver.find_element(*DatabasePage.version_select))
        select.select_by_visible_text(version)

    # Click Proceed button
    def proceed(self):
        self.driver.find_element(*DatabasePage.proceed_button).click()

    # Click return button
    def click_return(self):
        self.driver.find_element(*DatabasePage.return_button).click()

    # Verify file has been downloaded
    def verify_file_download(self):
        pass  # TODO

    # Click Upload button
    def upload(self):
        self.driver.find_element(*DatabasePage.upload_button).click()

    # Click Upload File button
    def upload_file(self):
        self.driver.find_element(*DatabasePage.upload_file_button).click()

    # Input filename
    def get_file(self, filepath):
        print(os.getcwd())
        self.driver.find_element(*DatabasePage.file_button).send_keys(os.getcwd() + filepath)

    # Click OK button
    def OK(self):
        self.driver.find_element(*DatabasePage.OK_button).click()

    # Verify that file has been uploaded
    def verify_file_upload(self):
        pass  # TODO
