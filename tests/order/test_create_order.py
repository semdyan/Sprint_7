import allure
import pytest

from methods.order_methods import OrderMethods

class TestCreateOrder:
    @allure.title('Проверка кода и текста ответа при успешном создании заказа с разным сочетанием цветов')
    @pytest.mark.parametrize('del_color', [0, 1, None])
    def test_create_order_success(self, generate_order_data, del_color):
        if del_color is not None:
            del generate_order_data['color'][del_color]
        else: pass
        status_code, response_json = OrderMethods.post_create_order(generate_order_data)
        assert isinstance(response_json, dict) and status_code == 201 and response_json['track'], \
            f'Вернулся неверный ответ: {status_code}, {response_json}'
