import requests
import allure

from data import Urls
from json import JSONDecodeError

class OrderMethods:

    @staticmethod
    @allure.step('Отправка запроса на создание заказа')
    def post_create_order(order_data):
        response = requests.post(url=f'{Urls.BASE_URL}{Urls.ORDER_URL}', json=order_data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @staticmethod
    @allure.step('Отправка запроса на получение списка заказов')
    def get_orders():
        response = requests.get(url=f'{Urls.BASE_URL}{Urls.ORDER_URL}')
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

