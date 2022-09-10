import json

from requests import Response
from utils.api import Google_maps_api
from utils.checking import Checking



"""Creating, alteration and removing new location"""
class Test_create_place():

    def test_created_place(self):
        print("\n POST method")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        token = json.loads(result_post.text)
        print(list(token))
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', "OK")

        print("GET method from POST")
        result_get: Response = Google_maps_api.get_created_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print("PUT method")
        print(place_id)
        result_put: Response = Google_maps_api.alter_location_information(place_id)
        Checking.check_status_code(result_put, 200)
        token = json.loads(result_put.text)
        print(list(token))
        Checking.check_json_token(result_put, ['msg'])

        print("GET method check PUT")
        result_get: Response = Google_maps_api.get_created_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', "BASHKORTOSTAN")

        print("DELETE")
        result_delete: Response = Google_maps_api.delete_location(place_id)
        Checking.check_status_code(result_delete, 200)
        token = json.loads(result_delete.text)
        print(list(token))
        Checking.check_json_token(result_delete, ['status'])

        print("GET method check DELETE")
        result_get: Response = Google_maps_api.get_created_place(place_id)
        Checking.check_status_code(result_get, 404)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value_content(result_get, 'msg', "doesn't exists")

