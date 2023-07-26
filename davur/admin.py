from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Restaurant_review)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(NullItem)
admin.site.register(ListOrder)
admin.site.register(Customer)
admin.site.register(FilterDate)

# For online customer
admin.site.register(ListOrderOnline)
admin.site.register(OrderOnline)
admin.site.register(NullItemOnline)
admin.site.register(CartItemOnline)
admin.site.register(CartOnline)
admin.site.register(CustomerHistory)
admin.site.register(ShippingAddress)
admin.site.register(Product_review)
admin.site.register(Discount)
admin.site.register(OrderTracking)






