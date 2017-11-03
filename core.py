import unittest
from myDriver import *
from elements import *


# create a new Firefox session

class test_exam(unittest.TestCase):
    def setUp(self):
        self.driver = myDriver("chrome")
        # testing git

    def test_for_exam(self):
        # navigate to the application home page
        google_page = googlePage(self.driver)
        self.driver.navigate("http://www.google.com")

        # submit search
        google_page.search_key("Seleniumhq")
        google_page.search_bar

        # click result
        google_page.click(google_page.result_seleniumHQ)

    def tearDown(self):
        self.driver.exit()


if __name__ == '__main__':
    unittest.main()