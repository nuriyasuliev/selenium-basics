from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
url = 'http://automationpractice.com'
driver.get(url)
sleep(15)
driver.find_element(By.XPATH, "//a[text()='Contact us']").click()
try:
    Element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Contact us']")))
except TimeoutException:
    print('Waited for 15 sec, could not locate the element')
else:
    Element.click()    
