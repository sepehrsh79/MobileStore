from django.contrib import admin
from .models import Mobile

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['model', 'price', 'color', 'is_available']

    class Meta:
        model = Mobile
