import time
import allure
import pytest
from locators import Locators
from pages.about_rent_page import AboutRent
from pages.base_page import BasePage
from pages.order_scooter_page import OrderScooter
from conftest import driver


class Test:

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('При нажатии на стрелочку/вопрос, открывается соответствующий текст.')
    @pytest.mark.parametrize('id_strelca,hidden_text', [[Locators.first_button, Locators.first_hidden_text],
                                                        [Locators.second_button, Locators.second_hidden_text],
                                                        [Locators.three_button, Locators.three_hidden_text],
                                                        [Locators.four_button, Locators.four_hidden_text],
                                                        [Locators.five_button, Locators.five_hidden_text],
                                                        [Locators.six_button, Locators.six_hidden_text],
                                                        [Locators.seven_button, Locators.seven_hidden_text],
                                                        [Locators.eight_button, Locators.eight_hidden_text]
                                                        ])
    def test_list_questions(self, driver, id_strelca, hidden_text):
        object_base_page = BasePage(driver)
        object_base_page.go_base_page()
        object_base_page.click_button(BasePage.button_cookie)
        object_base_page.scrol(id_strelca)
        object_base_page.checking_drop_down_list(id_strelca, hidden_text)
        assert object_base_page.find_element(hidden_text).is_displayed()

    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Проверка полного сценария от нажатия кнопки Заказать(любой) до отображения окна Заказ оформлен')
    @pytest.mark.parametrize('name, surname, address, telephone, station, button_order',
                             [['Дима','Фамилия','Москва','79864561223','Зорге', OrderScooter.button_order_down],
                             ['Вова', 'Петров', 'Академическая, 14 корп.2 кв. 133','89868542125','Преображенская площадь', OrderScooter.button_order_up]
                              ])
    def test_form_order(self, driver, name, surname, address, telephone, station, button_order):
        """ немного не понял задание, поэтому сделал как есть, если будут добавляться ещё кнопки Заказать их также можно будет использовать"""
        object_order = OrderScooter(driver)
        object_order.go_base_page()
        object_order.click_button(BasePage.button_cookie)
        object_order.click_button_order(button_order)
        object_order.input_values_page_for_who_scooter(name, surname, address, telephone, station)

        object_rent = AboutRent(driver)
        object_rent.page_about_rent_input_values()
        object_rent.window_want_place_order()

        assert object_rent.waiting(AboutRent.button_view_status_window_order_placed)

    @allure.title('Проверка кликабельности логотипа Самокат')
    @allure.description('При клике на логотип Самокат происходит переход на главную страницу Самоката')
    def test_button_scooter(self, driver):
        object_order = OrderScooter(driver)
        object_order.go_base_page()
        object_order.click_button_order(OrderScooter.button_order_down)
        object_order.waiting(OrderScooter.fild_name)
        object_order.click_button(OrderScooter.button_scooter)
        assert object_order.waiting(OrderScooter.button_order_up)

    @allure.title('Проверка кликабельности логотипа Яндекс')
    @allure.description('При клике на логотип Яндекс в новом окне через редирект откроется главная страница Дзена')
    def test_button_yandex(self, driver):
        object_order = OrderScooter(driver)
        object_order.go_base_page()
        object_order.waiting(BasePage.button_yandex_page_scooter)
        object_order.click_button(BasePage.button_yandex_page_scooter)
        object_order.driver.switch_to.window(object_order.driver.window_handles[1])
        time.sleep(5)   # поставил данное ожидание, т к пока не подобрал нужное, чтобы дождаться полной загрузки страницы

        assert object_order.get_url_page() == 'https://dzen.ru/?yredirect=true'







