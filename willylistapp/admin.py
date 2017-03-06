from django.contrib import admin

# Register your models here.
from willylistapp.models import Restaurant

admin.site.register(Restaurant) # add Restaurant object into admin.site
