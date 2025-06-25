from selenium.webdriver.support.wait import WebDriverWait



def wait_until_load(self):
    WebDriverWait(self.driver, 3)