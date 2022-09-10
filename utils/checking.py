"""Methods for responses checking"""
import json

from requests import Response

class Checking():

    """Status code checking method"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code  # сравнение желаемого статуса с полученным
        if response.status_code == status_code:
            print("Passed - Status code: " + str(response.status_code))
        else: print("Failed - Status code: " + str(response.status_code))


    """Cheching of required parameters in response"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All tokens present")

    """Checking token's content"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " right")

    @staticmethod
    def check_json_value_content(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутствует")
        else: print("Содержимое поля не соответствует")



