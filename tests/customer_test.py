from subscriptions.customer import Customer

customer_api = Customer()

# All customers
# print(customer_api.get_list_customers_by_Email("rosalin.d@wiseskool.com"))

# Get customer with email id
# print(customer_api.get_customer_by_Email("sangram.bng@gmail.com"))

# Get customer with id
# print(customer_api.get_customer_by_id("2004477000000071072"))

# Update customer
# print(customer_api.update_customer("2004477000000071072", data={"display_name": "quintus labs pvt.Ltd", 'email':'rosalin.d@wiseskool.com'}))

# Create Customer
# print(customer_api.create_customer(data={'display_name': 'quintus1995', 'email': 'biswaji.bm@gmail.com'}))


