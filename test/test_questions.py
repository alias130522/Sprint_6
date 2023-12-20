import allure
import pytest

from locators import Locators
from pages.main_page import MainPage
from conftest import driver
from urls import Urls

class TestQuestions:

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