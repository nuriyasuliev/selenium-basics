from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/') 

print(f' Title of the page is {driver.title}')
print(f'We are working on the {driver.name}')
print(driver.current_url)
print('Accepted usernames' in driver.page_source)