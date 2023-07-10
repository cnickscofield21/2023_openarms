from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    fields = [
        'first_name', 'last_name'
    ]

admin.site.register(Client, ClientAdmin)