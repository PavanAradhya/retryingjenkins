from selenium.webdriver import Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import time

@pytest.fixture()
def start():
    global driver
    caps = DesiredCapabilities().CHROME
    caps['pageLoadStrategy'] = 'eager'
    path = "./Drivers/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    yield
    driver.close()

def test_login(start):
    driver.find_element_by_xpath("//label[text()='Login']").click()
    driver.find_element_by_xpath("//input[@name='_txtUserName']").send_keys("test")
    driver.find_element_by_xpath("//input[@name='_txtPassword']").send_keys("test")
    driver.find_element_by_xpath("//input[@value='Login']").click()
    time.sleep(5)
    assert driver.current_url=="https://www.thetestingworld.com/testings/dashboard.php"





