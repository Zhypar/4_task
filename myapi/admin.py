from django.contrib import admin
from .models import Category, Branch, Contact, Course

admin.site.register(Category)
admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Course)