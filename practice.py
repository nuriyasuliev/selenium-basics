from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://automationpractice.com/')
# driver.find_element(By.ID, 'search_quary_top').send_keys('dress')
# driver.find_element(By.NAME, 'submit_search').click()
# driver.find_element(By.ID, 'SubmitLogin').click()
# driver.find_element(By.LINK_TEXT, 'Forgot your password').click()
# print('Retrieve' in driver.page_source
driver.find_element(By.LINK_TEXT, 'DRESSES').click()
print('There are 5 products' in driver.page_source)

# driver.find_elements(By.XPATH, "//span[text]()='Add to cart']"
add_buttons = driver.find_elements(By.CLASS_NAME,'product_container')
print(f'There are {len(add_button)} products displayed')
# print(len(add_button))
add_buttons[0].click()
driver.find_element(By.NAME, 'Submit').click()
print('There is 1 item in your cart' in driver.page_source)