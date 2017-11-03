from myDriver import *
from selenium.webdriver.common.by import By


#Creamos una clase con lo que vamos a usar  en google
class googlePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.ID, "lst-ib")
        self.search_button = (By.NAME, "btnK")
        self.result_seleniumHQ = (By.LINK_TEXT, "Selenium - Web Browser Automation")

    def search_key(self, text_to_search):
        self.driver.write_and_return(self.search_bar, text_to_search)
        self.driver.wait()

    def click(self, button):
        self.driver.click(button)
        self.driver.wait()




