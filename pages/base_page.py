import allure

from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class BasePage:
    """ класс общих методов """

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Осуществляем переход на выбранную страницу Самокат {url}')
    def go_base_page(self, url):
        return self.driver.get(url)

    @allure.step('Получение url отображаемой страницы')
    def get_url_page(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Найти элемент и кликнуть на него')
    def find_element_and_click(self, element):
        return self.driver.find_element(*element).click()

    @allure.step('Найти элемент и вернуть его значение')
    def find_element(self, element):
        return self.driver.find_element(*element)

    @allure.step('Скрол до выбранного элемента')
    def scrol(self, visible_element):
        element = self.driver.find_element(*visible_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание отображения элемента')
    def waiting(self, wait):
        return WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(wait))

    @allure.step('Ожидание кликабельности  выбранного элемента')
    def wait_clickable_element(self, click_element):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(click_element))

    # @allure.step('Найти элемент
    # def click_button(self, button):
    #     return self.driver.find_element(*button).click()

    @allure.step('Переключается на новое окно')
    def new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ожидание url')
    def wait_for_url(self, expected_url, attempts_count=20, attempt_timeout=0.3):
        """Ждет ссылку 20 раз по 0.3 секунды и возвращает её"""
        current_url = self.driver.current_url
        for _ in range(attempts_count):
            sleep(attempt_timeout)
            current_url = self.driver.current_url
            if expected_url in current_url:
                break
        return current_url
