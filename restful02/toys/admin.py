from django.contrib import admin
from .models import Toy


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'release_date', 'was_included_in_home']
    list_filter = ['created', 'release_date']
    search_fields = ['name', 'description']
