import unittest
from test_GMail import GmailLogin
import os
import HTMLTestRunner


def main():
    login_tests = unittest.TestLoader().loadTestsFromTestCase(GmailLogin)

    # Put them in the Array
    smoke_test = unittest.TestSuite([login_tests])

    dir = os.getcwd()

    # outfile = open(dir + '\SmokeTestReport1.html', "w")

    # runner = HTMLTestRunner.HTMLTestRunner(title='Test Report', description='Smoke Tests')
    # runner.run(smoke_test)

    fp = file('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner( stream=fp, title='My unit test', description='This demonstrates the report output by HTMLTestRunner.' )
    runner.run(smoke_test)


if __name__ == "__main__":
    main()
