import ast
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


class Invoice:
    def __init__(self, config=None):
        if config is None:
            self.client = Client(configuration.ZOHO_SUBSCRIPTION_CONFIG)
        else:
            self.client = Client(config)

    def list_invoices_by_customer(self,customer_id):
        cache_key = "zoho_invoices_%s" % customer_id
        response = self.client.get_from_cache(cache_key)
        if response is None:
            invoices_by_customer_uri = 'invoices?customer_id=%s' % customer_id
            result = self.client.send_request("GET", invoices_by_customer_uri)
            if type(result) is HTTPError:
                result_bytes = result.response._content
                result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
                return result_dict['message']
            else:
                response = result['invoices']
                self.client.add_to_cache(cache_key, response)
        else:
            print("Returning from cache : " + cache_key)
        return response

    def get_invoice(self,invoice_id):
        cache_key = "zoho_invoices_%s" % invoice_id
        response = self.client.get_from_cache(cache_key)
        if response is None:
            invoice_by_invoice_id_uri = 'invoices/%s'%invoice_id
            result = self.client.send_request("GET", invoice_by_invoice_id_uri)
            if type(result) is HTTPError:
                result_bytes = result.response._content
                result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
                return result_dict['message']
            else:
                response = result['invoice']
                self.client.add_to_cache(cache_key, response)
        else:
            print("Returning from cache : " + cache_key)

        return response

    def get_invoice_pdf(self,invoice_id):
        data = {'query': {'accept': 'pdf'}}
        invoice_pdf_by_invoice_id_uri = 'invoices/%s'%invoice_id
        headers = {"Accept": "application/pdf"}
        result = self.client.send_request("GET", invoice_pdf_by_invoice_id_uri,data=data, headers=headers)
        if type(result) is HTTPError:
            result_bytes = result.response._content
            result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
            return result_dict['message']
        return result

