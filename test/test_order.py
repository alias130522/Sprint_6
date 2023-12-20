import allure
import pytest

from pages.about_rent_page import AboutRent
from data import ORDER_DATA
from pages.order_scooter_page import OrderScooter
from conftest import driver
from urls import Urls

class TestOrder:

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








