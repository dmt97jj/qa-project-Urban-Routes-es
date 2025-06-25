import data
from helpers import retrieve_phone_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #localizadores test2
    taxi_button = (By.XPATH,'//button[@class="button round"]')
    comfort_button = (By.XPATH, '//div[@class="tcard-title" and contains(text(),"Comfort")]')


    #localizadores test3
    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.XPATH, '//input[@id="phone"]')
    next_button = (By.XPATH, '(//button[@class="button full"])[1]')
    phone_code_field = (By.XPATH, '//input[@id="code" and @class="input"]')
    confirm_button = (By.XPATH, '//button[@class="button full" and text()= "Confirmar"]')

    #localizadores test4
    pay_method_button = (By.XPATH, '//div[@class="pp-text"]')
    card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.CLASS_NAME, 'card-input')
    card_code_field = (By.XPATH, '//input[@id="code" and @name="code"]')
    add_button = (By.XPATH, '(//button[@class="button full"])[4]')
    close_button = (By.XPATH, '(//button[@class="close-button section-close"])[3]')

    #localizadores test5
    message_to_driver_field = (By.XPATH, '//input[@id="comment"]')

    #localizadores test6
    manta_pañuelos_button = (By.XPATH, '(//span[@class="slider round"][1])')

    #localizadores test7
    add_icecream_button = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    #localizadores test8
    window_info = (By.XPATH, '//div[@class="order-body"]')
    confirm_trip_button = (By.CLASS_NAME, 'smart-button-secondary')






    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #Métodos Test 2
    def select_taxi(self):
        self.driver.find_element(*self.taxi_button).click()
    def select_comfort(self):
        self.driver.find_element(*self.comfort_button).click()


    #Métodos Test 3
    def click_phone_button(self):
        self.driver.find_element(*self.phone_number_button).click()
    def input_phone_number(self):
        self.driver.find_element(*self.phone_number_field).send_keys(data.phone_number)
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()
    def input_phone_code(self):
        self.driver.find_element(*self.phone_code_field).send_keys(retrieve_phone_code(self.driver))
    def confirm_code_button(self):
        self.driver.find_element(*self.confirm_button).click()
    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')


    #Métodos Test 4
    def open_pay_method(self):
        self.driver.find_element(*self.pay_method_button).click()
    def add_card_button(self):
        self.driver.find_element(*self.card_button).click()
    def input_card_number(self):
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)
    def input_card_code(self):
        self.driver.find_element(*self.card_code_field).send_keys(data.card_code)
    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()
    def close_window(self):
        self.driver.find_element(*self.close_button).click()
    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')
    def get_card_code(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    #Métodos Test 5
    def write_message_to_driver(self):
        self.driver.find_element(*self.message_to_driver_field).send_keys('Muéstrame el camino al museo')
    def get_message(self):
        return self.driver.find_element(*self.message_to_driver_field).get_property('value')

    #Métodos Test 6
    def pedir_manta_pañuelos(self):
        self.driver.find_element(*self.manta_pañuelos_button).click()

    #Métodos Test 7
    def add_icecream(self):
        self.driver.find_element(*self.add_icecream_button).click()

    #Métodos Test 8
    def wait_for_window_info(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.window_info))
    def confirm_trip(self):
        self.driver.find_element(*self.confirm_trip_button).click()




class atajos:
    def set_both_address(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)

    def taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_taxi()

    def comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort()


    def add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_button()
        routes_page.input_phone_number()
        routes_page.click_next_button()
        routes_page.input_phone_code()
        routes_page.confirm_code_button()

    def add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_pay_method()
        routes_page.add_card_button()
        routes_page.input_card_number()
        routes_page.input_card_code()
        routes_page.click_add_button()
        routes_page.close_window()

    def message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_message_to_driver()


    def manta_pañuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.pedir_manta_pañuelos()

    def icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_icecream()
