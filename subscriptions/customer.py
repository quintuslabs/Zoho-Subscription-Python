import ast
import hashlib
import json

from requests import HTTPError

from client.client import Client

try:
    from urllib.parse import urlencode, quote
except:
    from urllib import urlencode, quote

try:
    from django.conf import settings as configuration

except ImportError:
    try:
        import config as configuration
    except ImportError:
        print("Zoho configurations not found in config/django settings, must be passed while initializing")


# class Customer:
#     def __init__(self, client):
#         self.client = client


class Customer:
    def __init__(self, config=None):
        if config is None:
            self.client = Client(configuration.ZOHO_SUBSCRIPTION_CONFIG)
        else:
            self.client = Client(config)

    def get_list_customers_by_Email(self, customer_email):
        cache_key = 'zoho_customer_%s' % hashlib.md5(customer_email.encode('utf-8')).hexdigest()
        response = self.client.get_from_cache(cache_key)
        if response is None:
            list_of_customers_by_Email_uri = 'customers?email=%s' % customer_email
            result = self.client.send_request("GET", list_of_customers_by_Email_uri)
            response = result['customers']
            self.client.add_to_cache(cache_key, response)
        else:
            print("Returning from cache : " + cache_key)

        return response

    def get_customer_by_Email(self, customer_email):
        customers = self.get_list_customers_by_Email(customer_email)
        if len(customers) == 0:
            return {"message": f"customer with email {customer_email} not found"}
        return self.get_customer_by_id(customers[0]['customer_id'])

    def get_customer_by_id(self, customer_id):
        cache_key = 'zoho_customer_%s' % customer_id
        response = self.client.get_from_cache(cache_key)
        if response is None:
            customer_by_customer_id_uri = 'customers/%s' % customer_id
            result = self.client.send_request("GET", customer_by_customer_id_uri)
            if type(result) is HTTPError:
                result_bytes = result.response._content
                result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
                return result_dict['message']
            else:
                response = result['customer']
                self.client.add_to_cache(cache_key, response)
        else:
            print("Returning from cache : " + cache_key)

        return response

    def update_customer(self, customer_id, data):
        cache_key = 'zoho_customer_%s' % customer_id
        headers = {'Content-type': 'application/json'}
        update_customer_by_customer_id = 'customers/%s' % customer_id
        result = self.client.send_request("PUT", update_customer_by_customer_id, data=data, headers=headers)
        if type(result) is HTTPError:
            result_bytes = result.response._content
            result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
            return result_dict['message']
        if result['code'] == 0:
            customer_val = result['customer']
            self.delete_customer_cache(cache_key)
            return customer_val
        else:
            return None

    def delete_customer_cache(self, cache_key_by_id):
        result = self.client.delete_from_cache(cache_key_by_id)
        return result

    def create_customer(self, data):
        headers = {'Content-type': 'application/json'}
        result = self.client.send_request("POST", 'customers', data=data, headers=headers)
        if type(result) is HTTPError:
            result_bytes = result.response._content
            result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
            return result_dict['message']
        else:
            if result.get('customer'):
                customer = result['customer']
                return customer


