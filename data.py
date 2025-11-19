class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIER_URL = 'courier/'
    ORDER_URL = 'orders/'

class Messages:
    message_create_courier_400 = 'Недостаточно данных для создания учетной записи'
    message_create_courier_409 = 'Этот логин уже используется. Попробуйте другой.'
    message_login_courier_400 = 'Недостаточно данных для входа'
    message_login_courier_404 = 'Учетная запись не найдена'

scooter_colors = [['BLACK'], ['GREY'], ['BLACK', 'GREY']]