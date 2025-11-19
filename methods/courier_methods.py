import allure
import requests

from data import Urls
from json import JSONDecodeError

class CourierMethods:
    @staticmethod
    @allure.step('Отправка запроса на регистрацию курьера')
    def post_create_courier(user_data):
        response = requests.post(url=f'{Urls.BASE_URL}{Urls.COURIER_URL}', json=user_data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @staticmethod
    @allure.step('Отправка запроса на аутентификацию курьера')
    def post_login_courier(user_data):
        response = requests.post(url=f'{Urls.BASE_URL}{Urls.COURIER_URL}login', json=user_data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @staticmethod
    @allure.step('Отправка запроса на удаление курьера')
    def delete_courier(user_data):
        user_id = CourierMethods.post_login_courier(user_data)[1]['id']
        response = requests.delete(url=f'{Urls.BASE_URL}{Urls.COURIER_URL}:id', json=user_id)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

