import allure
import pytest

from methods.courier_methods import CourierMethods
from data import Messages

class TestCreateCourier:

    @allure.title('Проверка кода и текста ответа при успешном создании курьера')
    def test_create_courier_success(self, generate_user_data):
        status_code, response_json = CourierMethods.post_create_courier(generate_user_data)
        assert status_code == 201 and response_json == {"ok": True}, \
            f'Вернулся неверный ответ: {status_code}, {response_json}'
        CourierMethods.delete_courier(generate_user_data)

    @allure.title('Проверка кода и текста ответа при попытке создания уже существующего курьера')
    def test_create_courier_existing_user_error(self, register_and_return_user_data):
        user_data = next(register_and_return_user_data)
        status_code, response_json = CourierMethods.post_create_courier(user_data)
        assert status_code == 409 and response_json['message'] == Messages.message_create_courier_409, \
            f'Вернулся неверный ответ: {status_code}, {response_json}'

    @allure.title('Проверка кода и текста ответа при попытке создания курьера без обязательного поля')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field_error(self, generate_user_data, missing_field):
        generate_user_data.pop(missing_field)
        status_code, response_json = CourierMethods.post_create_courier(generate_user_data)
        assert status_code == 400 and response_json['message'] == Messages.message_create_courier_400, \
            f'Вернулся неверный ответ: {status_code}, {response_json}'