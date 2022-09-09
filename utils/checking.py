"""Methods for responses checking"""
from requests import Response

class Checking():

    """Status code checking method"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code  # сравнение желаемого статуса с полученным
        if response.status_code == status_code:
            print("Passed - Status code: " + str(response.status_code))
        else: print("Failed - Status code: " + str(response.status_code))

