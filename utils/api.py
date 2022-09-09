from builtins import print

from utils.http_method import Http_methods

"""Methods for Google maps API testing"""

base_url = "https://rahulshettyacademy.com"  # Базовая URl
key = "?key=qaclick123"  # Параметр для всх запросов


class Google_maps_api():
    """New location creating method"""

    @staticmethod
    def create_new_place():
        json_create_new_location = {
            "location": {
                "lat": 2222222,
                "lng": 3333333
            },
            "accuracy": 50,
            "name": "Akmal IUNUSOV",
            "phone_number": "123456",
            "address": "Happy street, 19a building",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://vk.com",
            "language": "English"
        }
        post_resource = "/maps/api/place/add/json"  # Ресурс метода POST
        post_url= base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_create_new_location)
        print(result_post.text)
        return result_post


    @staticmethod
    def get_created_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def alter_location_information(place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        put_json = {
            "place_id": place_id,
            "address": "BASHKORTOSTAN",
            "key": "qaclick123"
        }
        result_put = Http_methods.put(put_url, put_json)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_location(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        delete_json = {
            "place_id": place_id,
                    }
        result_delete = Http_methods.delete(delete_url, delete_json)
        print(result_delete.text)
        return result_delete

