import allure
import pytest

from data import Messages
from helpers import generate_random_string
from methods.courier_methods import CourierMethods

class TestLoginCourier:
    def test_login_courier_success(self, register_and_return_user_data):
        user_data = next(register_and_return_user_data)
        status_code, response_json = CourierMethods.post_login_courier(user_data)
        assert status_code == 200 and response_json['id'], \
            f'Вернулся неверный ответ: {status_code}, {response_json}'

    @allure.title('Проверка кода и текста ответа при успешной аутентификации')
    @pytest.mark.xfail(reason="504 Timeout")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_field_error(self, register_and_return_user_data, missing_field):
        user_data_missing = next(register_and_return_user_data)
        user_data_missing.pop(missing_field)
        status_code, response_json = CourierMethods.post_login_courier(user_data_missing)
        assert status_code == 400 and response_json['message'] == Messages.message_login_courier_400, \
            f'Вернулся неверный ответ: {status_code}, {response_json}'

    @allure.title('Проверка кода и текста ответа при аутентификации с некорректными данными')
    @pytest.mark.parametrize("incorrect_field", ["login", "password"])
    def test_login_courier_incorrect_field_error(self, register_and_return_user_data, incorrect_field):
        user_data_incorrect = next(register_and_return_user_data)
        user_data_incorrect[incorrect_field] += generate_random_string(10)
        status_code, response_json = CourierMethods.post_login_courier(user_data_incorrect)
        assert status_code == 404 and response_json['message'] == Messages.message_login_courier_404, \
            f'Вернулся неверный ответ: {status_code}, {response_json}'

    @allure.title('Проверка кода и текста ответа при аутентификации незарегистрированного курьера')
    def test_login_courier_not_exists_error(self, generate_user_data):
        status_code, response_json = CourierMethods.post_login_courier(generate_user_data)
        assert status_code == 404 and response_json['message'] == Messages.message_login_courier_404, \
            f'Вернулся неверный ответ: {status_code}, {response_json}'