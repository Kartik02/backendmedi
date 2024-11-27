from app.models import Order

# Replace 101, 103, 104, 108, 107 with the primary keys mentioned in the error message
orders = Order.objects.filter(pk__in=[101, 103, 104, 108, 107])

# Print the objects found
print(orders)
