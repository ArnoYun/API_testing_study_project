from requests import Response
from utils.api import Google_maps_api




"""Creating, alteration and removing new location"""
class Test_create_place():

    def test_created_place(self):
        print("POST method")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("GET method from POST")
        result_get: Response = Google_maps_api.get_created_place(place_id)

        print("PUT method")
        print(place_id)
        result_put: Response = Google_maps_api.alter_location_information(place_id)

        print("GET method check PUT")
        result_get: Response = Google_maps_api.get_created_place(place_id)

        print("DELETE")
        result_get: Response = Google_maps_api.delete_location(place_id)

        print("GET method check DELETE")
        result_get: Response = Google_maps_api.get_created_place(place_id)