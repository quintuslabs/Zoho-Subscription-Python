from subscriptions.addon import Addon

ZOHO_SUBSCRIPTION_CONFIG = {
    "authtoken" : "a6dcaf1159317655a96b1f7838b35ac0",
    "zohoOrgId" : "695466261 ",
}

addon_api = Addon(ZOHO_SUBSCRIPTION_CONFIG)

# All Plans
# print(addon_api.list_addons())

# Plans with name or addon_code
# print(addon_api.list_addons(filters={"name": "Channel", "addon_code": "1101"}))

# Plans with plan_code
# print(addon_api.get_addon(1101))

