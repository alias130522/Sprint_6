import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    """ класс главной страницы """

    button_yandex_page_scooter = [By.XPATH, './/img[@src="/assets/ya.svg"][@alt="Yandex"]']
    button_scooter = [By.XPATH, './/img[@src="/assets/scooter.svg"][@alt="Scooter"]']
    url_page_yandex = 'https://dzen.ru/?yredirect=true'
    button_cookie = [By.ID, 'rcc-confirm-button']
    dzen = [By.XPATH, './/a[@class="desktop-base-header__logoLink-aE"][@data-testid="logo"]']


    @allure.step('Метод проверки выпадающего списка вопросов:'
                 'Клик/согласие на куки, '
                 'скрол до искомого элемента, '
                 'находит элемент списка, '
                 'кликает на него и ожидает появления скрытого текста')
    def checking_drop_down_list(self, id_arrow, click_element):
        self.find_element_and_click(MainPage.button_cookie)
        self.scrol(id_arrow)
        self.find_element_and_click(id_arrow)
        self.wait_clickable_element(click_element)



