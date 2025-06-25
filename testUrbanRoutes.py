
import data
from selenium import webdriver

import waitHelpers
from data import phone_number, card_number, card_code, message_for_driver
from urbanRoutesPage import UrbanRoutesPage
from urbanRoutesPage import atajos
import requests



class TestUrbanRoutes:

    driver = None

    # ESTE METODO FUNCIONA PARA SELENIUM >= 4.6
    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        atajos.set_both_address(self)
        address_from = data.address_from
        address_to = data.address_to
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        #test 2
    def test_select_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        atajos.set_both_address(self)
        waitHelpers.wait_until_load(self)
        atajos.taxi(self)
        waitHelpers.wait_until_load(self)
        atajos.comfort(self)
        response = requests.get(data.urban_routes_url)
        assert response.status_code == 200



        # test 3
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        atajos.set_both_address(self)
        phone_number =data.phone_number
        atajos.taxi(self)
        waitHelpers.wait_until_load(self)
        atajos.comfort(self)
        waitHelpers.wait_until_load(self)
        atajos.add_phone_number(self)
        assert routes_page.get_phone_number() == phone_number

        #test 4
    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        atajos.set_both_address(self)
        routes_page.select_taxi()
        waitHelpers.wait_until_load(self)
        atajos.add_card(self)
        assert routes_page.get_card_number() == card_number
        assert routes_page.get_card_code() == card_code


        #test 5
    def test_write_message_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        atajos.set_both_address(self)
        atajos.taxi(self)
        waitHelpers.wait_until_load(self)
        atajos.message(self)
        assert routes_page.get_message() == message_for_driver

        #test 6

    def test_pedir_manta_y_pañuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        atajos.set_both_address(self)
        waitHelpers.wait_until_load(self)
        atajos.taxi(self)
        waitHelpers.wait_until_load(self)
        routes_page.select_comfort()
        atajos.manta_pañuelos(self)
        response = requests.get(data.urban_routes_url)
        assert response.status_code == 200

        # test 7
    def test_two_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        atajos.set_both_address(self)
        waitHelpers.wait_until_load(self)
        atajos.taxi(self)
        waitHelpers.wait_until_load(self)
        atajos.comfort(self)
        atajos.icecream(self)
        waitHelpers.wait_until_load(self)
        atajos.icecream(self)
        response = requests.get(data.urban_routes_url)
        assert response.status_code == 200


        # test 8

    def test_wait_info_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        atajos.set_both_address(self)
        waitHelpers.wait_until_load(self)
        atajos.taxi(self)
        waitHelpers.wait_until_load(self)
        atajos.comfort(self)
        atajos.add_card(self)
        routes_page.write_message_to_driver()
        atajos.manta_pañuelos(self)
        atajos.icecream(self)
        atajos.add_phone_number(self)
        routes_page.confirm_trip()
        routes_page.wait_for_window_info()
        response = requests.get(data.urban_routes_url)
        assert response.status_code == 200

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()