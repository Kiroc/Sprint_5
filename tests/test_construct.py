from locators import *
from helpers import *

class TestConstructorPage:

    # переход к разделу «Булки»
    def test_transition_to_bun_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*LocatorsMain.sauces_btn).click()
        driver.find_element(*LocatorsMain.bun_btn).click()
        bun_text = driver.find_element(*LocatorsMain.bun).text
        bun_displayed = driver.find_element(*LocatorsMain.bun_ul).is_displayed()

        assert bun_text == 'Булки' and bun_displayed

    # переход к разделу «Соусы»
    def test_transition_to_sauces_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*LocatorsMain.sauces_btn).click()
        souces = driver.find_element(*LocatorsMain.sauces).text
        souces_displayed = driver.find_element(*LocatorsMain.sauces_ul).is_displayed()

        assert souces == 'Соусы' and souces_displayed

    # переход к разделу «Начинки»
    def test_transition_to_topping_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*LocatorsMain.toppings_btn).click()
        topping = driver.find_element(*LocatorsMain.topping).text
        topping_displayed = driver.find_element(*LocatorsMain.topping_ul).is_displayed()

        assert topping == 'Начинки' and topping_displayed

