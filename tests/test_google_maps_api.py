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


        print("GET method from POST")
        result_get: Response = Google_maps_api.get_created_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("PUT method")
        print(place_id)
        result_put: Response = Google_maps_api.alter_location_information(place_id)
        Checking.check_status_code(result_put, 200)

        print("GET method check PUT")
        result_get: Response = Google_maps_api.get_created_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("DELETE")
        result_delete: Response = Google_maps_api.delete_location(place_id)
        Checking.check_status_code(result_delete, 200)

        print("GET method check DELETE")
        result_get: Response = Google_maps_api.get_created_place(place_id)
        Checking.check_status_code(result_get, 200)