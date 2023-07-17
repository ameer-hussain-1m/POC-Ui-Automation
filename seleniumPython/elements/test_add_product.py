import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .browserActions import clickElement,sendKeysWithWait


class testAddProduct(unittest.TestCase):
    global driver
    def initialize_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://release.via.market/staff/login")

    def fillUpLoginForm(self):
        self.driver.find_element(By.NAME, "phone").clear()
        self.driver.find_element(By.NAME, "phone").send_keys("5125125120")
        self.driver.find_element(By.NAME, "code").send_keys("1234")
        self.driver.find_element(By.XPATH, "//div/button[@role='button']").click()
        self.driver.implicitly_wait(10)


    def setUp(self):
        self.initialize_driver()
        self.fillUpLoginForm()

    def test_if_the_product_is_added(self):
        driver=self.driver
        # test_if_application_is_opened(driver)
        clickElement(driver,"//div/button[@aria-label='Open site navigation menu']","xpath")
        clickElement(driver,"//div/h3[contains(text() , 'Products')]",'xpath')
        clickElement(driver,"//div/a[contains(text() , 'New product')]", "xpath")
        sendKeysWithWait(driver,"name","name","Automation Python")
        sendKeysWithWait(driver,"//div/textarea[@name='description']","xpath","Automation Python desc")
        sendKeysWithWait(driver,"//div/label[contains(text(),'Price')]/following-sibling::div/input","xpath","213")
        clickElement(driver,"//div/button[text()='Add']","xpath")
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()