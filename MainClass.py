import unittest
from test_GMail import GmailLogin
import HTMLTestRunner


def main():
    login_tests = unittest.TestLoader().loadTestsFromTestCase(GmailLogin)

    # Put them in the Array
    smoke_test = unittest.TestSuite([login_tests])

    fp = file('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Gmail Login Test',
                                           description='Report for Gmail Login Test.')
    runner.run(smoke_test)


if __name__ == "__main__":
    main()
