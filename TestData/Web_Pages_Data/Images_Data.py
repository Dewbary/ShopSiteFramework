from selenium.webdriver.common.by import By


class ImagesPage:

    def __init__(self, driver):
        self.driver = driver

    # \\-------------------- Locators --------------------//
    upload_images_button = (By.CSS_SELECTOR, "#button_upload_images")
    choose_file_button = (By.CSS_SELECTOR, "input[id='file_0']")
    upload_save_button = (By.CSS_SELECTOR, "input[name='upload.x']")
    image_list = (By.CSS_SELECTOR, "select[id='files']")

    # Click Upload button
    def upload_images(self):
        self.driver.find_element(*ImagesPage.upload_images_button).click()

    # Upload test image to file input
    def file_upload(self, file_name):
        file_btn = self.driver.find_element(*ImagesPage.choose_file_button)
        file_btn.send_keys(file_name)

    # "Send or be sent" - Brendan Dewberry
    # Click upload button in the file selection window
    def send(self):
        self.driver.find_element(*ImagesPage.upload_save_button).click()

    # Get text from list of images
    def get_image_list(self):
        img_list = self.driver.find_element(*ImagesPage.image_list)
        print(img_list.text)
        return img_list.text
