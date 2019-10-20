


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium import FirefoxDriver;


user = "test@test.com"  #These will not log in.
pwd = "testtest"  #These will not log in.

# driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path='/Library/Frameworks/Python.framework/Versions/3.7/bin/geckodriver')


driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()