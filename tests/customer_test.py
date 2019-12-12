from subscriptions.customer import Customer
from subscriptions.plan import Plan

customer_api = Customer()

# All customers
print(customer_api.get_list_customers_by_Email("rosalin.d@wiseskool.com"))

# print(customer_api.get_customer_by_Email("sangram.bng@gmail.com"))

# print(customer_api.get_customer_by_id("2004477000000071072"))
# print(customer_api.update_customer("2004477000000071072", data={"display_name": "quintus apps pvt ltd",'email':'rosalin.d@wiseskool.com'}))

# Create Customer
# print(customer_api.create_customer(data={'display_name': 'plutonic', 'email' : 'sangram@quintus.com'}))
