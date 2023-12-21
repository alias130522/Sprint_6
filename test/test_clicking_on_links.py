import allure

from pages.main_page import MainPage
from pages.order_scooter_page import OrderScooter
from conftest import driver
from urls import Urls

class TestClickinglinks:

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