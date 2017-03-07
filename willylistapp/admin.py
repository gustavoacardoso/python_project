from django.contrib import admin

# Register your models here.
from willylistapp.models import Restaurant, Customer, Driver, Meal, Order, OrderDetails

admin.site.register(Restaurant) # add Restaurant object into admin.site
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetails)
