from subscriptions.addon import Addon

addon_api = Addon()

# All Plans
# print(addon_api.list_addons())

# Plans with name or addon_code
print(addon_api.list_addons(filters={"name": "", "addon_code": ""}))

# Get addon with addon code
# print(addon_api.get_addon(1101))

