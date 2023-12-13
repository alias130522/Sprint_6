import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait, time
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

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

    def click_button_order(self, button):
        """ клик на кнопку Заказать внизу страницы и сверху """
        element = self.driver.find_element(*button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(5)
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(button))
        return self.driver.find_element(*button).click()


    def input_data(self, name, surname, address, telephone):
        """ заполнение полей ввода формы Для кого самокат"""
        self.driver.find_element(*self.fild_name).send_keys(name)
        self.driver.find_element(*self.fild_surname).send_keys(surname)
        self.driver.find_element(*self.fild_address).send_keys(address)
        self.driver.find_element(*self.fild_telephone).send_keys(telephone)

    def choose_metro_station(self, station):
        """ выбор станции метро из поля Станция метро страницы Для кого самокат"""
        self.driver.find_element(*self.fild_metro_station).click()
        (WebDriverWait(self.driver, 100).until
         (EC.visibility_of_element_located((By.CLASS_NAME, 'select-search__select'))))
        self.driver.find_element(*self.fild_metro_station).send_keys(station)
        self.driver.find_element(*self.drop_down_list_metro_station).click()


    # def click_button_next(self):
    #     """ клик кнопки Далее на странице Для кого самокат"""
    #     return self.driver.find_element(*self.button_next).click()

    def input_values_page_for_who_scooter(self, name, surname, address, telephone, station):
        """ полный сценарий заполнения данных на странице Для кого самокат """
        self.waiting(OrderScooter.fild_name)
        self.input_data(name, surname, address, telephone)
        self.choose_metro_station(station)
        self.click_button(OrderScooter.button_next)

