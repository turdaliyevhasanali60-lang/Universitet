from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    list_filter = ('yonalish', 'asosiy',)
    search_fields = ('nom',)

@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'aktiv']
    search_fields = ['nom']
    list_filter = ['aktiv']

@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    search_fields = ('ism',)