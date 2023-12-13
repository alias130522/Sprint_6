import allure
from locators import Locators
from selenium.webdriver.common.by import By
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    """ класс общих методов и теста первой страницы """

    button_yandex_page_scooter = [By.XPATH, './/img[@src="/assets/ya.svg"][@alt="Yandex"]']
    button_scooter = [By.XPATH, './/img[@src="/assets/scooter.svg"][@alt="Scooter"]']
    url_page_yandex = 'https://dzen.ru/?yredirect=true'
    button_cookie = [By.ID, 'rcc-confirm-button']

    def __init__(self, driver):
        self.driver = driver
        self.base_url = Locators.BASE_URL

    def go_base_page(self):
        """ переход на главную страницу """
        return self.driver.get(self.base_url)

    def get_url_page(self):
        """ получение url отображаемой страницы """
        current_url = self.driver.current_url
        return current_url

    def find_element_and_click(self, id_element):
        """ найти элемент по его id и кликнуть """
        return self.driver.find_element(*id_element).click()

    def find_element(self, xpath_element):
        """ найти элемент и вернуть его значение """
        return self.driver.find_element(*xpath_element)


    def scrol(self, visible_element):
        """ скрол главной страницы вниз до выбранного элемента """
        element = self.driver.find_element(*visible_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def waiting(self, wait):
        """ ожидание отображения выбранного элемента """
        return WebDriverWait(self.driver, 100).until(expected_conditions.visibility_of_element_located(wait))


    def click_button(self, button):
        """ клик на любую кнопку """
        return self.driver.find_element(*button).click()

    def checking_drop_down_list(self, id_arrow, wait):
        """ находит элемент списка, кликает на него и ожидает появления скрытого текста"""
        self.find_element_and_click(id_arrow)
        self.waiting(wait)
