import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage


class OrderScooter(BasePage):
    """ работа с формой Для кого самокат """

    button_order_up = [By.XPATH, './/button[@class="Header_Link__1TAG7"]/preceding-sibling::button']
    button_order_down = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/child::button']

    fild_name = [By.XPATH, './/input[@placeholder="* Имя"]']
    fild_surname = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    fild_address = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    fild_telephone = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    fild_metro_station = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    drop_down_list_metro_station = [By.CLASS_NAME, 'select-search__select']
    button_next = [By.XPATH, './/button[text()="Далее"]']

    @allure.step('Клик на кнопку Заказать {button} внизу/сверху страницы')
    def click_button_order(self, button):
        """ клик на кнопку Заказать внизу страницы и сверху """
        self.scrol(button)
        self.waiting(button)
        return self.find_element_and_click(button)


    def input_data(self, name, surname, address, telephone):
        """ заполнение полей ввода формы Для кого самокат"""
        self.get_fild_name(name)
        self.get_fild_surname(surname)
        self.get_fild_address(address)
        self.get_fild_telephone(telephone)

    def get_fild_name(self, name):
        """ возврат поля Имя с вводимым аргументом формы Для кого самокат """
        return self.find_element(OrderScooter.fild_name).send_keys(name)

    def get_fild_surname(self, surname):
        """ возврат поля Фамилия с вводимым аргументом формы Для кого самокат """
        return self.find_element(OrderScooter.fild_surname).send_keys(surname)

    def get_fild_address(self, address):
        """ возврат поля Адрес с вводимым аргументом формы Для кого самокат """
        return self.find_element(OrderScooter.fild_address).send_keys(address)

    def get_fild_telephone(self, telephone):
        """ возврат поля Телефон с вводимым аргументом формы Для кого самокат """
        return self.find_element(OrderScooter.fild_telephone).send_keys(telephone)

    def choose_metro_station(self, station):
        """ выбор станции метро из поля Станция метро страницы Для кого самокат"""
        self.find_element_and_click(OrderScooter.fild_metro_station)
        self.waiting(OrderScooter.drop_down_list_metro_station)
        self.find_element(OrderScooter.fild_metro_station).send_keys(station)
        self.find_element_and_click(OrderScooter.drop_down_list_metro_station)


    @allure.step('Метод заполнения данных на стр Для кого самокат объединяет: '
                 'клик/согласие на куки, '
                 'ожидание страницы Для кого самокат, '
                 'заполнение полей: Имя, Фамилия, Адрес, Станция метро, Телефон'
                 'клик на кнопку Далее ')
    def input_values_page_for_who_scooter(self, name, surname, address, telephone, station):
        self.find_element_and_click(MainPage.button_cookie)
        self.waiting(OrderScooter.fild_name)
        self.input_data(name, surname, address, telephone)
        self.choose_metro_station(station)
        self.find_element_and_click(OrderScooter.button_next)

