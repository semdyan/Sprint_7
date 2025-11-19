import allure
import pytest

from methods.order_methods import OrderMethods
from data import scooter_colors

class TestCreateOrder:
    @allure.title('Проверка кода и текста ответа при успешном создании заказа с одним из цветов')
    @pytest.mark.parametrize('add_color', scooter_colors)
    def test_create_order_different_colors_success(self, generate_order_data, add_color):
        generate_order_data['color'] = add_color
        status_code, response_json = OrderMethods.post_create_order(generate_order_data)
        assert isinstance(response_json, dict) and status_code == 201 and response_json['track'], \
            f'Вернулся неверный ответ: {status_code}, {response_json}'

    @allure.title('Проверка кода и текста ответа при успешном создании заказа без указания цвета')
    def test_create_order_no_colors_success(self, generate_order_data):
        status_code, response_json = OrderMethods.post_create_order(generate_order_data)
        assert isinstance(response_json, dict) and status_code == 201 and response_json['track'], \
            f'Вернулся неверный ответ: {status_code}, {response_json}'