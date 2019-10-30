#from subscriptions.subscription import Subscription
from subscriptions.invoice import Invoice

ZOHO_SUBSCRIPTION_CONFIG = {
    "authtoken" : "a6dcaf1159317655a96b1f7838b35ac0",
    "zohoOrgId" : "695466261 ",
}

#subscriptions = Subscription(ZOHO_SUBSCRIPTION_CONFIG)
#print(subscriptions.list_subscriptions_by_customer("2004477000000071072"))


#print(subscriptions.list_subscriptions_by_customer("2004477000000071072"))
#print (subscriptions.get_subscriptions("2004477000000071085"))
invoices = Invoice(ZOHO_SUBSCRIPTION_CONFIG)
#print (invoices.list_invoices_by_customer("2004477000000071072"))
#'invoice_id': '2004477000000086003'
print (invoices.get_invoice("2004477000000086003"))