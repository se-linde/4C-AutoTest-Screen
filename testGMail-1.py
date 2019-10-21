from StdSuites import event
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from selenium import FirefoxDriver;

# Change to YouTube Test Account
user = "microdwaynedev@gmail.com"
pwd = "Faceraigi1!"

# driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path='/Library/Frameworks/Python.framework/Versions/3.7/bin/geckodriver')

driver.get("https://www.youtube.com")

# Setting the size so the window is smaller.
# Did this so that I could adequately see the interpreter
# error messages behind the window. 

# driver.set_window_size(1088, 788)

sleep(20)

# Now, click on the 'Sign In' button on the top right.

elem = driver.find_element_by_id("text")

sleep(20)

elem.click()

sleep(20)

assert "YouTube" in driver.title

elem = driver.find_element_by_id(pwd)

sleep(20)

elem.send_keys(user)
sleep(5)

elem.send_keys(Keys.RETURN)

# Get sleep working. This works!
sleep(20)
# event.wait does not work.
# event(elem).wait(5)

# This crashes; poss. solution here:
# https://stackoverflow.com/questions/49864965/org-openqa-selenium-elementnotinteractableexception-element-is-not-reachable-by


elem = driver.find_element_by_id("password")

elem.send_keys("Faceraigi1!")
# event().wait(1)

# Get sleep working.
sleep(20)

elem.send_keys(Keys.RETURN)

# Get sleep working.
sleep(20)

driver.close()
