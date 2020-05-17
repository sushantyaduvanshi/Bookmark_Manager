from django.contrib import admin

# Register your models here.

from .models import Customer, Bookmarks, customer_bookmark

admin.site.register(Customer)
admin.site.register(Bookmarks)
admin.site.register(customer_bookmark)