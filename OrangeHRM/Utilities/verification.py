from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


path = r"../defects"

def screenshot(driver):
    d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    driver.save_screenshot(f"{path}/{d}.png")



def verify_title(driver,wp_title):
    wait = WebDriverWait(driver,10)
    try:
        wait.until(EC.title_is(wp_title))
    except:
        assert driver.title == wp_title,screenshot(driver)
        print("Title is matching")

def verify_url(driver,url):
    wait = WebDriverWait(driver,10)
    try:
        wait.until(EC.url_to_be(url))
    except:
        assert driver.driver.current_url == url, screenshot(driver)
        print("Title is matching")