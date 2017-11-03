class Button(object):
    name = ""
    target = ""
    value = ""

    def __init__(self, name, target, value, driver):
        self.name = name
        self.target = target
        self.value = value
        self.driver = driver

    def click(self, element):
        self.driver.click(element)


def make_button(name, target, value, driver):
    button = Button(name, target, value, driver)
    return button


class Checkbox(object):
    name = ""
    target = ""
    value = ""

    def __init__(self, name, target, value, driver):
        self.name = name
        self.target = target
        self.value = value
        self.driver = driver

    def click(self, element):
        self.driver.click(element)


def make_checkbox(name, target, value, driver):
    checkbox = Checkbox(name, target, value, driver)
    return checkbox


class InputArea(object):
    name = ""
    target = ""
    value = ""

    def __init__(self, name, target, value, driver):
        self.name = name
        self.target = target
        self.value = value
        self.driver = driver

    def click(self, element):
        self.driver.click(element)

    def clear(self, element):
        self.driver.get_elements()


def make_input_area(name, target, value, driver):
    inputarea = InputArea(name, target, value, driver)
    return inputarea


searchBar = make_input_area("search", "id", "lst-ib", driver )