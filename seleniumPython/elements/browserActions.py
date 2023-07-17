
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def clickElement(driver,locator,locatorType):
    if(locatorType == 'name'):
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, locator)))
        element.click()

    if(locatorType == 'xpath'):
         driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.XPATH, locator))
         element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, locator)))
         time.sleep(3)
         element.click()

def sendKeysWithWait(driver,locator,locatorType,text):
     if(locatorType == 'name'):
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, locator)))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        element.send_keys(text)

     if(locatorType == 'xpath'):
         driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, locator))
         element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, locator)))
         element.click()
         element.send_keys(text)