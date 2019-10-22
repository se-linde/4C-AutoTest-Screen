# Imported libraries.

import unittest
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# These will try to get reports going.
import HtmlTestRunner

# Try this as a tutorial - test reference notes:
# https://scrolltest.com/2015/04/30/selenium-test-case-in-python/

# https://testingbot.com/support/getting-started/pyunit.html

# https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test

class SeleniumTestGmailLogin(unittest.TestCase):

    def setUp(self):
        # GMail Test Account
        user = "microdwaynedev@gmail.com"
        pwd = "Micrraigi1!"
        driver = webdriver.Firefox(executable_path='/Library/Frameworks/Python.framework/Versions/3.7/bin/geckodriver')

    def test_gmail(self):
        # Putting this in to prevent race conditions, and to allow all of the elements
        # on the page to be found.

        driver = self.driver
        driver.implicitly_wait(20)  # seconds.
        driver.get("https://www.gmail.com")
        driver.set_window_size(1088, 788)

        sleep(10)


        # Setting the size so the window is smaller.
        # Did this so that I could adequately see the interpreter
        # error messages behind the window.


        # Now, click on the 'Sign In' button on the top right.

        #elem = driver.find_element_by_class_name("h-c-header__nav-li-link ")

        # elem.click()


        # This makes sure that I am on the right page.
        assert "Gmail" in driver.title

        elem = driver.find_element_by_id("identifierId")

        elem.send_keys(self.setUp.user)

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

        elem.send_keys(self.setUp.pwd)

        sleep(20)


        # Get sleep working.

        elem.send_keys(Keys.RETURN)

        sleep(20)

    def tearDown(self):

        self.setUp.driver.close()


if __name__ == '__main__':

    unittest.main()