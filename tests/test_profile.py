from locators import *
from helpers import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestProfileArea:
    # переход по клику на «Личный кабинет»
    def test_transition_to_profile_from_main_page_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*LocatorsMain.login_account_btn).click()
        driver.find_element(*LocatorsAuth.email_input).send_keys(Reg.email)
        driver.find_element(*LocatorsAuth.password_input).send_keys(Reg.password)
        driver.find_element(*LocatorsAuth.login_account_btn).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsMain.personal_account_btn))
        driver.find_element(*LocatorsMain.personal_account_btn).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsProfile.exit_btn))
        save_btn_displayed = driver.find_element(*LocatorsProfile.save_btn).is_displayed()

        assert driver.current_url == URL_profile and save_btn_displayed

    # Переход из личного кабинета в конструктор
    def test_transition_from_profile_to_constructor_by_click_constructor_btn_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*LocatorsMain.login_account_btn).click()
        driver.find_element(*LocatorsAuth.email_input).send_keys(Reg.email)
        driver.find_element(*LocatorsAuth.password_input).send_keys(Reg.password)
        driver.find_element(*LocatorsAuth.login_account_btn).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsMain.personal_account_btn))
        driver.find_element(*LocatorsMain.personal_account_btn).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsProfile.exit_btn))
        driver.find_element(*LocatorsProfile.constructor_btn).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsMain.bun))
        bun_displayed = driver.find_element(*LocatorsMain.bun).is_displayed()

        assert driver.current_url == URL_auth and bun_displayed

    # Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_transition_from_profile_to_constructor_by_click_logo_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*LocatorsMain.login_account_btn).click()
        driver.find_element(*LocatorsAuth.email_input).send_keys(Reg.email)
        driver.find_element(*LocatorsAuth.password_input).send_keys(Reg.password)
        driver.find_element(*LocatorsAuth.login_account_btn).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsMain.personal_account_btn))
        driver.find_element(*LocatorsMain.personal_account_btn).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsProfile.exit_btn))
        driver.find_element(*LocatorsProfile.logo_btn).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsMain.bun))
        bun_displayed = driver.find_element(*LocatorsMain.bun).is_displayed()

        assert driver.current_url == URL_auth and bun_displayed

        # Проверка выхода из личного кабинета
    def test_logout_from_profile_success(self, driver):
        driver.get(URL_main)
        driver.find_element(*LocatorsMain.login_account_btn).click()
        driver.find_element(*LocatorsAuth.email_input).send_keys(Reg.email)
        driver.find_element(*LocatorsAuth.password_input).send_keys(Reg.password)
        driver.find_element(*LocatorsAuth.login_account_btn).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsMain.personal_account_btn))
        driver.find_element(*LocatorsMain.personal_account_btn).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsProfile.exit_btn))
        driver.find_element(*LocatorsProfile.exit_btn).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsAuth.login_account_btn))
        login_btn_displayed = driver.find_element(*LocatorsAuth.login_account_btn).is_displayed()

        assert driver.current_url == URL_auth and login_btn_displayed
        