from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#Configuracion general del wait, normalemente no lo utilizaria es solo para propositos de demo
wait_time = 3

# Definiamos la creeacion sel driver
class myDriver:
    def __init__(self,browser):
        if browser.upper() == "CHROME":
            self.driver = webdriver.Chrome()
        elif browser.upper() == "FIREFOX":
            firefoxCap = DesiredCapabilities.FIREFOX
            firefoxCap['marionette'] = True
            self.driver = webdriver.Firefox(capabilities = firefoxCap)
        else:
            print("Please select FIREFOX or CHROME")
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()


        
#Defino las funciones a utilizar algunas
    def wait(self):
        sleep(wait_time)

    def navigate(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(15)

    def click(self,element):
        self.driver.find_element(*element).click()

    def write(self,element,text_to_send):
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(text_to_send)

    def write_and_return(self,element,text_to_send):
        self.write(element,text_to_send)
        self.driver.find_element(*element).send_keys(Keys.RETURN)    

    def getEle(self,locator,reason):
        elem = {
        "ID": self.driver.find_element_by_id(locator),
        "CLASS": self.driver.find_element_by_class_name(locator),
        "NAME": self.driver.find_element_by_name(locator),
        "XPATH": self.driver.find_element_by_xpath(locator)
         }
        
        return elem[reason.upper()]()

    def get_elements(self,element):
        return self.driver.find_elements(*element)
    
    def exit(self):
        self.driver.quit()
