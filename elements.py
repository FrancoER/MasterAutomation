from myDriver import *
from selenium.webdriver.common.by import By


class googlePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.ID, "lst-ib")
        self.search_button = (By.NAME, "btnK")
        self.result_links = (By.CLASS_NAME, "r")

    def search_key(self, text_to_search):
        self.driver.write_and_return(self.search_bar, text_to_search)

    def get_links(self):
        return self.driver.get_elements(self.result_links)


class Button(object):
    name = ""
    target = ""
    value = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, target, value, driver):
        self.name = name
        self.target = target
        self.value = value
        self.driver = driver

    def click(self, element):
        self.driver.click(element)


def make_button(name, target, value):
    button = Button(name, target, value)
    return button


class Checkbox(object):
    name = ""
    target = ""
    value = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, target, value, driver):
        self.name = name
        self.target = target
        self.value = value
        self.driver = driver

    def click(self, element):
        self.driver.click(element)


def make_checkbox(name, target, value):
    checkbox = Checkbox(name, target, value)
    return checkbox


class InputArea(object):
    name = ""
    target = ""
    value = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, target, value, driver):
        self.name = name
        self.target = target
        self.value = value
        self.driver = driver

    def click(self, element):
        self.driver.click(element)

    def clear(self, element):
        self.driver.


def make_input_area(name, target, value):
    checkbox = InputArea(name, target, value)
    return checkbox