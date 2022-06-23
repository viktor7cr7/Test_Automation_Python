from utils.http_method import Http_method

"""Методы для тестирования Google_maps_api"""       #Получение ответа от сервера и составление запроса

url = 'https://rahulshettyacademy.com'              #базовая url
key = '?key=qaclick123'

                                                    #Метод для создания новой локации
class Google_maps_api():

    @staticmethod
    def create_new_place():

        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json'   #Ресурс метода post
        post_url  = url+post_resource+key
        print(post_url)
        result_post = Http_method.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_check_new_place(place_id):

        resource_get = '/maps/api/place/get/json'
        check_get = url + resource_get + key + '&place_id=' + place_id
        print(check_get)
        result_get = Http_method.get(check_get)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_update_place(place_id):

        put_resource = '/maps/api/place/update/json'
        put_url =  url + put_resource + key

        put_body = {
            "place_id": place_id,
            "address": "Moscov , str Lenina , dom 77 RUS",
            "key": "qaclick123"
        }
        print(put_url)
        result_put = Http_method.put(put_url, body=put_body)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        resource_delete = '/maps/api/place/delete/json'
        url_delete = url + resource_delete + key

        body_delete = {
            "place_id": place_id
        }

        print(url_delete)
        delete_result = Http_method.delete(url_delete, body_delete)
        print(delete_result.text)
        return delete_result
