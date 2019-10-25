# Imported libraries.

import unittest
from logging import exception
from time import sleep, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class GmailLogin(unittest.TestCase):

    def setUp(self):

        # GMail Test Account
        self.user = "microdwaynedev@gmail.com"
        self.pwd = "Micrraigi1!"
        self.driver = webdriver.Firefox(
            executable_path='/Library/Frameworks/Python.framework/Versions/3.7/bin/geckodriver')

    def test_gmail(self):

        self.driver.implicitly_wait(20)  # seconds.

        try:
            self.driver.get("https://www.gmail.com")

        except IOError:
            print ("Error: website is not found.")

        self.driver.set_window_size(1088, 788)

        sleep(10)

        assert "Gmail" in self.driver.title
        elem = self.driver.find_element_by_id("identifierId")
        elem.send_keys(self.user)
        elem.send_keys(Keys.RETURN)

        sleep(5)

        elem = self.driver.find_element_by_xpath("//input[@name='password']")

        if elem is not None:
            sleep(5)
            elem.send_keys(self.pwd)
            sleep(5)

        else:
            print NoSuchElementException

        elem.send_keys(Keys.RETURN)
        sleep(5)

    def tearDown(self):

        self.driver.close()


if __name__ == '__main__':
    # unittest.main()

    # test_class = SeleniumTestGmailLogin()

    # HTML test runner example: https://www.dev2qa.com/python-3-unittest-html-and-xml-report-example/

    unittest.main(verbosity=2)
