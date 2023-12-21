Sprint_6

class BasePage - класс общих методов и теста первой страницы
    
методы BasePage
go_base_page - переход на главную страницу
get_url_page - получение url отображаемой страницы
find_element_by_id_and_click - найти элемент по его id и кликнуть
find_element - найти элемент и вернуть его значение
scrol - скрол главной страницы вниз до выбранного элемента
waiting - ожидание отображения выбранного элемента
checking_drop_down_list - находит элемент списка, кликает на него и ожидает появления скрытого текста

Локаторы класса BasePage
button_yandex_page_scooter - логотип Яндекса на главной странице Самокат
button_scooter - логотип Самокат на главной странице Самокат
url_page_yandex - url страницы Дзен/Яндекс
button_cookie - кнопка Куки


class OrderScooter(BasePage) - класс работы с формой Для кого самокат

методы OrderScooter
click_button_order - клик на кнопку Заказать внизу страницы и сверху
input_data - заполнение полей ввода формы Для кого самокат
choose_metro_station - выбор станции метро из поля Станция метро страницы Для кого самокат
input_values_page_for_who_scooter - полный сценарий заполнения данных на странице Для кого самокат

Локаторы OrderScooter
button_order_up - кнопка Заказать сверху страницы
button_order_down - кнопка Заказать снизу страницы
fild_name - поле имя
fild_surname - поле фамилия
fild_address - поле адрес
fild_telephone - поле телефон
fild_metro_station - поле станция метро
drop_down_list_metro_station - выпадающий список станций метро
button_next - кнопка далее страницы Для кого самокат


class AboutRent(BasePage) - класс работы со страницей  Про аренду

методы AboutRent
get_today - заполнение поля Когда привести самокат на стр Про аренду
choice_rental_period - выбор Срока аренды самоката на стр Про аренду
input_checkbox_label - выбор чекбокса в поле Цвет самоката на стр Про аренду
page_about_rent_input_values - заполнение полей ввода страницы Про аренду
window_want_place_order - ожидание окна Хотите оформить аренду и клик на кнопку Да

локаторы AboutRent
field_when_bring_scooter - поле Когда привести самокат
text_about_rent - текст заголовок страницы Про аренду
field_rental_period - поле Срок аренды
field_rental_period_text_two_days - Срок аренды выпадающий список срок двое суток
checkbox_black - чекбокс Чёрный жемчуг
button_order - кнопка заказать
button_yes_window_want_place_order - кнопка Да окна Хотите заказать самокат
button_view_status_window_order_placed - кнопка посмотреть статус окна Заказ оформлен

