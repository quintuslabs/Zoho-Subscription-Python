from subscriptions.subscription import Subscription


ZOHO_SUBSCRIPTION_CONFIG = {
    "authtoken" : "a6dcaf1159317655a96b1f7838b35ac0",
    "zohoOrgId" : "695466261 ",
}

subscriptions = Subscription(ZOHO_SUBSCRIPTION_CONFIG)

# print(subscriptions.list_subscriptions_by_customer("2004477000000071072"))
print (subscriptions.get_subscriptions("100"))
