from django.contrib import admin
from bookstore_app.models import Books,Category

# Register your models here.

admin.site.register(Books)
admin.site.register(Category)