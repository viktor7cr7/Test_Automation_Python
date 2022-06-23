import requests
from utils.logger import Logger

"""Список http методов"""
import allure

class Http_method():
    headers = {'Content-Type' : 'appclication/json'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step('GET'):
            Logger.add_requests(url,method='GET')
            result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)  #информация по запросу
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_requests(url,method='POST')
            result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_requests(url,method='PUT')
            result = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("delete"):
            Logger.add_requests(url,method='DELETE')
            result = requests.delete(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

