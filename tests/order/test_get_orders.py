import allure

from methods.order_methods import OrderMethods

class TestGetOrders:
    @allure.title('Проверка кода и текста ответа при получении списка заказов')
    def test_get_all_orders_success(self):
        status_code, response_json = OrderMethods.get_orders()
        assert status_code == 200 and 'orders' in response_json, \
            f'Вернулся неверный ответ: {status_code}, {response_json}'