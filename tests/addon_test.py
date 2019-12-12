from subscriptions.addon import Addon

addon_api = Addon()

# All Plans
# print(addon_api.list_addons())

# Plans with name or addon_code
# print(addon_api.list_addons(filters={"name": "Channel", "addon_code": "1101"}))

# Get addon with addon code
# print(addon_api.get_addon(1101))

