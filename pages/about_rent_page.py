import allure
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AboutRent(BasePage):
    """ методы страницы Про аренду"""

    field_when_bring_scooter = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    text_about_rent = [By.XPATH, './/div[text()="Про аренду"]']
    field_rental_period = [By.XPATH, './/div[text()="* Срок аренды"]']
    field_rental_period_text_two_days = [By.XPATH, './/div[text()="двое суток"]']
    checkbox_black = [By.ID, "black"]
    button_order = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"][text()="Заказать"]']
    button_yes_window_want_place_order = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"][text()="Да"]']
    button_view_status_window_order_placed = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"][text()="Посмотреть статус"]']


    def get_today(self):
        """ заполнение поля Когда привести самокат на стр Про аренду"""
        self.driver.find_element(*self.field_when_bring_scooter).click()
        data = str(datetime.date.today())
        self.driver.find_element(*self.field_when_bring_scooter).send_keys(data)
        self.driver.find_element(*self.text_about_rent).click()

    def choice_rental_period(self, number_days):
        """ выбор Срока аренды самоката на стр Про аренду"""
        self.driver.find_element(*self.field_rental_period).click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(number_days))
        self.driver.find_element(*self.field_rental_period_text_two_days).click()

    def input_checkbox_label(self, checkbox):
        """ выбор чекбокса в поле Цвет самоката на стр Про аренду"""
        return self.driver.find_element(*checkbox).click()

    @allure.step('Метод запонения данных стр Про аренду объединяет:'
                 'ожидание отображения страницы Про аренду,'
                 'установка действующей даты в поле Когда привести самокат,'
                 'выбор срока аренды,'
                 'выбор чекбокса,'
                 'клик на кнопку Заказать')
    def page_about_rent_input_values(self):
        self.waiting(AboutRent.field_when_bring_scooter)
        self.get_today()
        self.choice_rental_period(AboutRent.field_rental_period_text_two_days)
        self.input_checkbox_label(AboutRent.checkbox_black)
        self.click_button(AboutRent.button_order)

    @allure.step('Ожидание окна Хотите оформить аренду и клик на кнопку Да')
    def window_want_place_order(self):
        self.waiting(AboutRent.button_yes_window_want_place_order)
        self.click_button(AboutRent.button_yes_window_want_place_order)



