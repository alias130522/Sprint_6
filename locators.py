import allure
from selenium.webdriver.common.by import By


class Locators:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    first_button = By.ID, 'accordion__heading-0'
    first_hidden_text = By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]'

    second_button = By.ID, 'accordion__heading-1'
    second_hidden_text = By.XPATH, './/p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]'

    three_button = By.ID, 'accordion__heading-2'
    three_hidden_text = By.XPATH, './/p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]'

    four_button = By.ID, 'accordion__heading-3'
    four_hidden_text = By.XPATH, './/p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]'

    five_button = By.ID, 'accordion__heading-4'
    five_hidden_text = By.XPATH, './/p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]'

    six_button = By.ID, 'accordion__heading-5'
    six_hidden_text = By.XPATH, './/p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]'

    seven_button = By.ID, 'accordion__heading-6'
    seven_hidden_text = By.XPATH, './/p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]'

    eight_button = By.ID, 'accordion__heading-7'
    eight_hidden_text = By.XPATH, './/p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]'
