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

# https://stackoverflow.com/questions/20251386/pycharm-and-unittest-does-not-work

# https://github.com/se-linde/SeleniumTestWithPython/blob/master/UnitTest_Demo.py

class GmailLogin(unittest.TestCase):

    def setUp(cls):

        # GMail Test Account
        cls.user = "microdwaynedev@gmail.com"
        cls.pwd = "Micrraigi1!"
        cls.driver = webdriver.Firefox(executable_path='/Library/Frameworks/Python.framework/Versions/3.7/bin/geckodriver')


    def test_gmail(self):

        # Putting this in to prevent race conditions, and to allow all of the elements
        # on the page to be found.

        # driver = self.setUp.driver
        self.driver.implicitly_wait(20)  # seconds.
        self.driver.get("https://www.gmail.com")
        # Alternate URL: https://www.google.com/intl/en-US/gmail/about/

        self.driver.set_window_size(1088, 788)

        sleep(10)


        # Setting the size so the window is smaller.
        # Did this so that I could adequately see the interpreter
        # error messages behind the window.


        # Now, click on the 'Sign In' button on the top right.

        #elem = driver.find_element_by_class_name("h-c-header__nav-li-link ")

        # elem.click()


        # This makes sure that I am on the right page.
        assert "Gmail" in self.driver.title

        elem = self.driver.find_element_by_id("identifierId")

        elem.send_keys(self.user)

        elem.send_keys(Keys.RETURN)

        # Get sleep working. This works!

        # This crashes; poss. solution here:
        # https://stackoverflow.com/questions/49864965/org-openqa-selenium-elementnotinteractableexception-element-is-not-reachable-by

        # This is the class for the element of the box.
        # elem = driver.find_element_by_css_selector("HHWSud")

        # PASSWORD FIELD
        # XPATH relpath: //input[@name='password']

        sleep(5)

        elem = self.driver.find_element_by_xpath("//input[@name='password']")

        sleep(5)


        # This is the class for the element of the text field in the box.

        elem.send_keys(self.pwd)

        sleep(5)


        # Get sleep working.

        elem.send_keys(Keys.RETURN)

        sleep(5)

    # def tearDown(self):

        self.driver.close()


if __name__ == '__main__':

    # unittest.main()

    # test_class = SeleniumTestGmailLogin()

    # HTML test runner example: https://www.dev2qa.com/python-3-unittest-html-and-xml-report-example/

    unittest.main(verbosity=2)