import allure
import pytest
import requests

from helpers import generate_random_string, generate_random_number, generate_random_date
from methods.courier_methods import CourierMethods
from data import Urls

@pytest.fixture(scope='function', autouse=False)
@allure.step('Генерация данных пользователя')
def generate_user_data():
    user_data = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
    return user_data

@pytest.fixture(scope='function', autouse=False)
@allure.step('Генерация данных пользователя и регистрация курьера')
def register_and_return_user_data():

    user_data = {}

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    order_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_URL}', data=order_data)

    if response.status_code == 201:
        user_data['login'] = login
        user_data['password'] = password
        user_data['first_name'] = first_name

    yield user_data
    CourierMethods.delete_courier(user_data)

@pytest.fixture(scope='function', autouse=False)
@allure.step('Генерация данных заказа')
def generate_order_data():
    order_data = {'firstName': generate_random_string(10),
                  'lastName': generate_random_string(10),
                  'address': generate_random_string(10),
                  'metroStation': generate_random_string(10),
                  'phone': generate_random_string(10),
                  'rentTime': generate_random_number(2),
                  'deliveryDate': generate_random_date(),
                  'comment': generate_random_string(10)}

    return order_data