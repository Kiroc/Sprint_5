from locators import *
from helpers import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegister:

    # Успешная регистрация
    def test_registration_success(self, driver):
        driver = driver
        driver.get(URL_reg)
        RU = RandomUser()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LocatorsRegister.registration_btn))
        driver.find_element(*LocatorsRegister.name_input).send_keys(RU.user_name)
        driver.find_element(*LocatorsRegister.email_input).send_keys(RU.email)
        driver.find_element(*LocatorsRegister.password_input).send_keys(RU.password)
        driver.find_element(*LocatorsRegister.registration_btn).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LocatorsAuth.login_account_btn))
        login_btn_displayed = driver.find_element(*LocatorsAuth.login_account_btn).is_displayed()

        assert driver.current_url == URL_auth and login_btn_displayed

        # Проверка ошибки для некорректного пароля
    def test_registration_incorrect_password_check_error(self, driver):
        driver = driver
        driver.get(URL_reg)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsRegister.registration_btn))
        driver.find_element(*LocatorsRegister.name_input).send_keys(Reg.user_name)
        driver.find_element(*LocatorsRegister.email_input).send_keys(Reg.email)
        driver.find_element(*LocatorsRegister.password_input).send_keys(12345)
        driver.find_element(*LocatorsRegister.registration_btn).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_any_elements_located(
            LocatorsRegister.error_message_incorrect_password))
        error = driver.find_element(*LocatorsRegister.error_message_incorrect_password).text

        assert (error == 'Некорректный пароль') and (driver.current_url == URL_reg)




