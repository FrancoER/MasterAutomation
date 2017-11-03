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
        google_page.result_links

        # get the list of elements which are displayed after the search
        # currently on result page using find_elements_by_class_name  method
        lists = google_page.get_links()

        # get the number of elements found
        print("Found " + str(len(lists)) + " results:")
        # iterate through each element and print the text that is
        # name of the search
        for listitem in lists:
            print(listitem.text)

    def tearDown(self):
        self.driver.exit()


if __name__ == '__main__':
    unittest.main()
