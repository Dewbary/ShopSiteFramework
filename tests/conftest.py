import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/brendan/Documents/ShopSiteFramework/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Chrome(executable_path="exec_path")
    driver.get("http://brendanqa.com/cgi-bin/brendan/ss/start.cgi")
    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver

    username = "shopTest"
    password = "test123"

    driver.find_element_by_name("ss_id1").send_keys(username)
    driver.find_element_by_name("ss_pw1").send_keys(password)
    driver.find_element_by_name("login").click()
    time.sleep(2)

    yield

    driver.close()



