from locators import *
from main import *

class TestConstructorPage:

    # переход к разделу «Булки»
    def test_transition_to_bun_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*Locators_Main.sauces_btn).click()
        driver.find_element(*Locators_Main.bun_btn).click()
        bun_text = driver.find_element(*Locators_Main.bun).text
        bun_displayed = driver.find_element(*Locators_Main.bun_ul).is_displayed()

        assert bun_text == 'Булки' and bun_displayed

    # переход к разделу «Соусы»
    def test_transition_to_sauces_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*Locators_Main.sauces_btn).click()
        souces = driver.find_element(*Locators_Main.sauces).text
        souces_displayed = driver.find_element(*Locators_Main.sauces_ul).is_displayed()

        assert souces == 'Соусы' and souces_displayed

    # переход к разделу «Начинки»
    def test_transition_to_topping_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*Locators_Main.toppings_btn).click()
        topping = driver.find_element(*Locators_Main.topping).text
        topping_displayed = driver.find_element(*Locators_Main.topping_ul).is_displayed()

        assert topping == 'Начинки' and topping_displayed

