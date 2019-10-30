import json

from client.client import Client
from subscriptions.addon import Addon
from subscriptions.customer import Customer
from subscriptions.hostedpage import HostedPage
from subscriptions.invoice import Invoice
from subscriptions.plan import Plan
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

    def plan(self):
        return Plan(self.client)

    def customer(self):
        return Customer(self.client)

    def add_on(self):
        return Addon(self.client)

    def invoice(self):
        return Invoice(self.client)

    def hosted_page(self):
        return HostedPage(self.client)

    def list_invoices_by_customer(self,customer_id):
        cache_key = "zoho_invoices_%s" % customer_id
        response = self.client.get_from_cache(cache_key)
        if response is None:
            invoices_by_customer_uri = 'invoices?customer_id=%s' % customer_id
            result = self.client.send_request("GET", invoices_by_customer_uri)
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
            response = result['invoice']
            self.client.add_to_cache(cache_key, response)
        else:
            print("Returning from cache : " + cache_key)