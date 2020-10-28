from django.contrib import admin
from .models import Event, Category


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'name',
        'category',
        'image',
    )

    ordering = ('date',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)