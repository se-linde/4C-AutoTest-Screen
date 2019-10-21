from StdSuites import event
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium import FirefoxDriver;


# FB Test Account.
user = "microdwaynedev@gmail.com"
pwd = "Faceraigi1!"

# driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path='/Library/Frameworks/Python.framework/Versions/3.7/bin/geckodriver')


driver.get("https://www.facebook.com")

# Setting the size so the window is smaller.
# Did this so that I could adequately see the interpreter
# error messages behind the window.

driver.set_window_size(1088, 788)


# sleep to see each part of the script working.
# sleep(1);

assert "Facebook" in driver.title


elem = driver.find_element_by_id("email")

elem.send_keys(user)

# Get sleep working. This works!
sleep(20)
# event.wait does not work.
# event(elem).wait(5)

elem = driver.find_element_by_id("pass")

elem.send_keys(pwd)
# event().wait(1)

# Get sleep working.
sleep(20)


elem.send_keys(Keys.RETURN)


# Get sleep working.
sleep(20)


driver.close()