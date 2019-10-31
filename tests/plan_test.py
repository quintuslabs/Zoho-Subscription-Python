from subscriptions.plan import Plan

ZOHO_SUBSCRIPTION_CONFIG = {
    "authtoken" : "a6dcaf1159317655a96b1f7838b35ac0",
    "zohoOrgId" : "695466261 ",
}

plan_api = Plan(ZOHO_SUBSCRIPTION_CONFIG)

# All Plans
#print(plan_api.list_plans())

# Plans with name or plan_code
# print(plan_api.list_plans(filters={"name": 'Basic', "plan_code": ""}))

# Plans with plan_code
#print(plan_api.get_plan(1200))

# get price by plan_code
# print(plan_api.get_price_by_plan_code(1200))
# print (plan_api.get_addon_for_plan(1100))

#Get all addons for a plan
print (plan_api.get_addons_for_plan("1200"))