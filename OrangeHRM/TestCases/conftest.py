from selenium.webdriver import Chrome,ChromeOptions
from Utilities.verification import *
from time import sleep
import pytest


opts = ChromeOptions()
opts.add_experimental_option("detach",True)

base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
login_page_title = "OrangeHRM"


@pytest.fixture
def setup():
    driver = Chrome(opts)
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    verify_title(driver,login_page_title)
    yield driver
    sleep(2)
    driver.close()




