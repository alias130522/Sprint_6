
import allure
import pytest

from locators import Locators
from pages.about_rent_page import AboutRent
from pages.data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_scooter_page import OrderScooter
from conftest import driver
from pages.urls import Urls

class TestOrder:

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
        object_main_page = MainPage(driver)
        object_main_page.go_base_page(Urls.BASE_URL)
        object_main_page.checking_drop_down_list(id_strelca, hidden_text)
        assert object_main_page.find_element(hidden_text).is_displayed()

    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Проверка полного сценария от нажатия кнопки Заказать(любой) до отображения окна Заказ оформлен')
    @pytest.mark.parametrize('order_params', ORDER_DATA)
    def test_form_order(self, driver, order_params):
        object_order = OrderScooter(driver)
        object_order.go_base_page(Urls.BASE_URL)
        object_order.click_button_order(order_params['button_order'])
        object_order.input_values_page_for_who_scooter(order_params['name'], order_params['surname'], order_params['address'],
                                                       order_params['telephone'], order_params['station'])
        object_rent = AboutRent(driver)
        object_rent.page_about_rent_input_values()
        object_rent.window_want_place_order()
        assert object_rent.waiting(AboutRent.button_view_status_window_order_placed)


    @allure.title('Проверка кликабельности логотипа Самокат')
    @allure.description('При клике на логотип Самокат происходит переход на главную страницу Самоката')
    def test_button_scooter(self, driver):
        object_order = OrderScooter(driver)
        object_order.go_base_page(Urls.BASE_URL)
        object_order.click_button_order(OrderScooter.button_order_down)
        object_order.waiting(OrderScooter.fild_name)
        object_order.find_element_and_click(MainPage.button_scooter)
        assert object_order.waiting(OrderScooter.button_order_up)

    @allure.title('Проверка кликабельности логотипа Яндекс')
    @allure.description('При клике на логотип Яндекс в новом окне через редирект откроется главная страница Дзена')
    def test_button_yandex(self, driver):
        object_order = OrderScooter(driver)
        object_order.go_base_page(Urls.BASE_URL)
        object_order.waiting(MainPage.button_yandex_page_scooter)
        object_order.find_element_and_click(MainPage.button_yandex_page_scooter)
        object_order.new_window()
        assert object_order.wait_for_url(MainPage.url_page_yandex) == 'https://dzen.ru/?yredirect=true'







