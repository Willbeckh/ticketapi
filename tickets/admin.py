from django.contrib import admin
from .models import Ticket, Category
# Register your models here.

admin.site.register(Ticket)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
admin.site.register(Category, CategoryAdmin)