from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/') 

username_field = driver.find_element(By.ID, 'user-name')

password_field = driver.find_element(By.NAME, 'password')

login_button = driver.find_element(By.CLASS_NAME, 'submit-button')

username_field.send_keys('standard_user')

password_field.send_keys('secret_sauce')

login_button.click()

print('product' in driver.page_source)
