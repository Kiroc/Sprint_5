from locators import *
from main import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_in_login_btn_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*Locators_Main.login_account_btn).click()
        driver.find_element(*Locators_Auth.email_input).send_keys(Reg.email)
        driver.find_element(*Locators_Auth.password_input).send_keys(Reg.password)
        driver.find_element(*Locators_Auth.login_account_btn).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators_Main.place_order_button))
        order_btn = driver.find_element(*Locators_Main.place_order_button).text

        assert (driver.current_url == URL_main) and (order_btn == 'Оформить заказ')

    # вход через кнопку «Личный кабинет»
    def test_login_in_personal_account_btn_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*Locators_Main.personal_account_btn).click()
        driver.find_element(*Locators_Auth.email_input).send_keys(Reg.email)
        driver.find_element(*Locators_Auth.password_input).send_keys(Reg.password)
        driver.find_element(*Locators_Auth.login_account_btn).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators_Main.place_order_button))
        order_btn = driver.find_element(*Locators_Main.place_order_button).text

        assert (driver.current_url == URL_main) and (order_btn == 'Оформить заказ')

    # вход через кнопку в форме регистрации
    def test_login_in_register_success(self, driver):
        driver.get(URL_reg)
        driver.find_element(*Locators_Register.login_account_btn).click()
        driver.find_element(*Locators_Auth.email_input).send_keys(Reg.email)
        driver.find_element(*Locators_Auth.password_input).send_keys(Reg.password)
        driver.find_element(*Locators_Auth.login_account_btn).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators_Main.place_order_button))
        order_btn = driver.find_element(*Locators_Main.place_order_button).text

        assert (driver.current_url == URL_main) and (order_btn == 'Оформить заказ')

    # вход через кнопку в форме восстановления пароля
    def test_login_in_recover_success(self, driver):
        driver.get(URL_recover)
        driver.find_element(*Locators_Recover.login_account_btn).click()
        driver.find_element(*Locators_Auth.email_input).send_keys(Reg.email)
        driver.find_element(*Locators_Auth.password_input).send_keys(Reg.password)
        driver.find_element(*Locators_Auth.login_account_btn).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators_Main.place_order_button))
        order_btn = driver.find_element(*Locators_Main.place_order_button).text

        assert (driver.current_url == URL_main) and (order_btn == 'Оформить заказ')
