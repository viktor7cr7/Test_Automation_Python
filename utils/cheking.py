"""Методы для проверки ответов запросов"""
import json

from requests import Response


class Cheking():
    """Проверка статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Верно!, Статус код = " + str(response.status_code))
        else:
            print("Провал!, Статус код = " + str(response.status_code))

#"""Проверка наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")


    #Проверка значений обязательных полей в ответе запроса
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " Верен")



