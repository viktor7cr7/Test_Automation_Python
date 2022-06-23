import json
import allure

from requests import Response

from utils.api import Google_maps_api

"""Создание, изменение и удаление новой локации"""
from utils.cheking import Cheking
@allure.epic("Test_create_location")


class Test_create_place():

    @allure.description("Создание,изменение.проверка и удаление новой локации")
    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Cheking.check_status_code(result_post, 200)
        print(result_post.status_code)
        token = json.loads(result_post.text)
        print(list(token))
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK' )

        print("Метод GET")
        result_get: Response = Google_maps_api.get_check_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        toket_get = json.loads(result_get.text)
        print(list(toket_get))
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, "address", "29, side layout, cohen 09")



        print("Метод PUT")
        result_put: Response = Google_maps_api.put_update_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_value(result_put,'msg', 'Address successfully updated')



        print("Метод GET_PUT")
        result_get: Response = Google_maps_api.get_check_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_value(result_get, 'address', 'Moscov , str Lenina , dom 77 RUS')

        print("Метод DELETE")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete, ['status'])
        Cheking.check_json_value(result_delete,'status', 'OK')


        print("Метод GET_DELETE")
        result_get: Response = Google_maps_api.get_check_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_value(result_get,'msg', "Get operation failed, looks like place_id  doesn't exists")

