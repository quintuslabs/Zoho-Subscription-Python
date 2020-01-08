from subscriptions.plan import Plan

plan_api = Plan()

# All Plans
# print(plan_api.list_plans())

# Plans with name or plan_code
# print(plan_api.list_plans(filters={"name": '', "plan_code": ""}))

# Plans with plan_code
# print(plan_api.get_plan(1200))

# get price by plan_code
# print(plan_api.get_price_by_plan_code(1200))


# Get all addons for a plan
# print(plan_api.get_addons_for_plan("1100"))
