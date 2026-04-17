import pytest

from POM.loginpage import LoginPage
from Utilities.verification import *
from Utilities.XLUtils import *


data = read_data("Login_TestData")

@pytest.mark.parametrize("un,pas",data)
def test_tc001(setup,un,pas):
    if un == "Admin" and  pas == "admin123":
        driver = setup
        log = LoginPage(driver)
        log.usernaem_text_field(un)
        log.password_text_field(pas)
        log.login_button()
        verify_url(driver,"https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    else:
        driver = setup
        log = LoginPage(driver)
        log.usernaem_text_field(un)
        log.password_text_field(pas)
        log.login_button()
        verify_url(driver, "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
