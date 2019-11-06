from subscriptions.invoice import Invoice

ZOHO_SUBSCRIPTION_CONFIG = {
    "authtoken" : "a6dcaf1159317655a96b1f7838b35ac0",
    "zohoOrgId" : "695466261 ",
}
invoices = Invoice(ZOHO_SUBSCRIPTION_CONFIG)

print (invoices.list_invoices_by_customer("2004477000000071072"))
print (invoices.get_invoice("2004477000000086003"))
print (invoices.get_invoice_pdf("2004477000000086003"))