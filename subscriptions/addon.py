import ast

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


class Addon:
    def __init__(self, config=None):
        if config is None:
            self.client = Client(configuration.ZOHO_SUBSCRIPTION_CONFIG)
        else:
            self.client = Client(config)

    def list_addons(self, filters=None):
        cache_key = 'addons'
        response = self.client.get_from_cache(cache_key)
        if response is None:
            list_of_addons_uri = 'addons'
            result = self.client.send_request("GET", list_of_addons_uri)
            response = result['addons']
            self.client.add_to_cache(cache_key, response)

        if filters is not None:
            for addon in response:
                 if (addon['name'] == filters['name'] or addon['addon_code'] == filters['addon_code']):
                        return addon
        else:
            print("Returning from cache : " + cache_key)

        return response

    def get_addon(self, addon_code=None):
        cache_key = 'addon_%s' % addon_code
        response = self.client.get_from_cache(cache_key)
        if response is None:
            addon_by_addon_code = 'addons/%s' % addon_code
            result = self.client.send_request("GET", addon_by_addon_code)
            if type(result) is HTTPError:
                result_bytes = result.response._content
                result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
                return result_dict['message']
            else:
                response = result['addon']
                self.client.add_to_cache(cache_key, response)
        else:
            print("Returning from cache : " + cache_key)

        return response
