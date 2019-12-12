import ast
import json

from requests import HTTPError

from client.client import Client
from subscriptions import addon
from subscriptions.addon import Addon

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


class Plan:
    add_on_types = ['recurring', 'one_time', ]

    def __init__(self, config=None):
        if config is None:
            self.client = Client(configuration.ZOHO_SUBSCRIPTION_CONFIG)
        else:
            self.client = Client(config)

    def list_plans(self, filters=None, with_add_ons=True, add_on_type=None):
        cache_key = 'plans'
        response = self.client.get_from_cache(cache_key)
        if response is None:
            list_of_plan_uri = 'plans'
            result = self.client.send_request("GET", list_of_plan_uri)
            response = result['plans']
            self.client.add_to_cache(cache_key, response)

        if filters is not None:
            for plan in response:
                if (plan['name'] == filters['name'] or plan['plan_code'] == filters['plan_code']):
                    return plan

        # if with_add_ons is not None:
        #     if with_add_ons in add_on_type:
        #         return None
        else:
            print("Returning from cache : " + cache_key)
        return response

    def get_plan(self, plan_code):
        cache_key = 'plan_%s' % plan_code
        response = self.client.get_from_cache(cache_key)
        if response is None:
            plan_by_plan_code = 'plans/%s' % plan_code
            result = self.client.send_request("GET", plan_by_plan_code)
            if type(result) is HTTPError:
                result_bytes = result.response._content
                result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
                return result_dict['message']
            else:
                response = result['plan']
                self.client.add_to_cache(cache_key, response)
        else:
            print("Returning from cache : " + cache_key)

        return response

    def get_addons_for_plan(self,plan_code):
        cache_key = 'plans'
        addon_code_list = []
        addon = Addon()
        response = self.client.get_from_cache(cache_key)
        if response is None:
            list_of_plan_uri = 'plans'
            result = self.client.send_request("GET", list_of_plan_uri)
            response = result['plans']
            self.client.add_to_cache(cache_key, response)
            if plan_code is not None:
                for each_plan in response:
                    if each_plan.get("addons"):
                        if each_plan.get('plan_code')== plan_code:
                            for each_addon_code in each_plan["addons"]:
                                addon_code_list.append(addon.get_addon(each_addon_code['addon_code']))
                return addon_code_list
            else:
                print("Returning from cache : " + cache_key)

    # Filter Plan

    def get_price_by_plan_code(self, plan_code):
        cache_key = 'plan_%s' % plan_code
        response = self.client.get_from_cache(cache_key)
        if response is None:
            plan_by_plan_code = 'plans/%s' % plan_code
            result = self.client.send_request("GET", plan_by_plan_code)
            if type(result) is HTTPError:
                result_bytes = result.response._content
                result_dict = ast.literal_eval(result_bytes.decode('utf-8'))
                return result_dict['message']
            else:
                response = result['plan']
                self.client.add_to_cache(cache_key, response)
                recurring_price = response['recurring_price']
                return recurring_price
        else:
            print("Returning from cache : " + cache_key)
        return response



