from StdSuites import event
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from selenium import FirefoxDriver;

# Change to YouTube Test Account
user = "microdwaynedev@gmail.com"
pwd = "Micrraigi1!"


# driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path='/Library/Frameworks/Python.framework/Versions/3.7/bin/geckodriver')

# Putting this in to prevent race conditions, and to allow all of the elements
# on the page to be found.

driver.implicitly_wait(20) #seconds.
driver.get("https://www.gmail.com")

# Setting the size so the window is smaller.
# Did this so that I could adequately see the interpreter
# error messages behind the window. 

driver.set_window_size(1088, 788)

sleep(10)

# Now, click on the 'Sign In' button on the top right.

#elem = driver.find_element_by_class_name("h-c-header__nav-li-link ")

# elem.click()


# This makes sure that I am on the right page.
assert "Gmail" in driver.title

elem = driver.find_element_by_id("identifierId")

elem.send_keys(user)

elem.send_keys(Keys.RETURN)

# Get sleep working. This works!

# This crashes; poss. solution here:
# https://stackoverflow.com/questions/49864965/org-openqa-selenium-elementnotinteractableexception-element-is-not-reachable-by

# This is the class for the element of the box.
# elem = driver.find_element_by_css_selector("HHWSud")

# PASSWORD FIELD
# XPATH relpath: //input[@name='password']

sleep(20)

elem = driver.find_element_by_xpath("//input[@name='password']")

sleep(20)


# This is the class for the element of the text field in the box.

elem.send_keys(pwd)

sleep(20)


# Get sleep working.

elem.send_keys(Keys.RETURN)

sleep(20)


# Get sleep working.

driver.close()
