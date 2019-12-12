import ast
import json

import requests
from cachetools import TTLCache
from requests import HTTPError

from utils.constants import DEFAULT_CACHE_MODE, DEFAULT_CACHE_TTL, ZOHO_AUTH_HEADER, ZOHO_AUTH_TOKEN_HEADER_PREFIX, \
    ZOHO_ORG_ID_HEADER, ZOHO_SUBSCRIPTION_API_URL, DEFAULT_CACHE_MAXSIZE


class Client:
    def __init__(self, config):
        self.auth_token = config["authtoken"]
        self.zoho_org_id = config["zohoOrgId"]
        try:
            self.cache_enabled = config["cache_enabled"]
        except KeyError:
            self.cache_enabled = DEFAULT_CACHE_MODE

        try:
            self.cache_ttl = config["cache_ttl"]
        except KeyError:
            self.cache_ttl = DEFAULT_CACHE_TTL
        self.requests = requests.Session()
        self.cache = TTLCache(ttl=self.cache_ttl, maxsize=DEFAULT_CACHE_MAXSIZE)

    def add_to_cache(self, key, value):
        if (self.cache_enabled is None) or (self.cache_enabled is False):
            pass
        else:
            self.cache[key] = value

    def get_from_cache(self, key):
        if (self.cache_enabled is None) or (self.cache_enabled is False):
            return None
        else:
            try:
                return self.cache[key]
            except KeyError:
                return None

    def delete_from_cache(self, key):
        if (self.cache_enabled is None) or (self.cache_enabled is False):
            return False
        else:
            try:
                self.cache.pop(key=key)
                return True
            except KeyError:
                return False
            # my_key = ast.literal_eval(key)
            # return self.cache.pop(key=key)

    def get_request_headers(self, headers):
        default_headers = {
            ZOHO_AUTH_HEADER: ZOHO_AUTH_TOKEN_HEADER_PREFIX + self.auth_token,
            ZOHO_ORG_ID_HEADER: self.zoho_org_id,
            'Content-Type': "application/json"
        }
        if (headers is not None) and len(headers) > 0:
            default_headers.update(headers)
        return default_headers

    def send_request(self, method, uri, data=None, headers=None):
        try:
            response = requests.request(method, ZOHO_SUBSCRIPTION_API_URL + uri, data=json.dumps(data),
                                        headers=self.get_request_headers(headers))
            response.raise_for_status()

        except HTTPError as http_err:
            return http_err
        except Exception as err:
            return None
        if response.headers['Content-Type'] == 'application/json;charset=UTF-8':
            return json.loads(response.text)
        else:
            return response.content

