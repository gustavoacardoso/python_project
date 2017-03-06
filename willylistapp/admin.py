from django.contrib import admin

# Register your models here.
from willylistapp.models import Restaurant, Customer, Driver, Meal

admin.site.register(Restaurant) # add Restaurant object into admin.site
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
