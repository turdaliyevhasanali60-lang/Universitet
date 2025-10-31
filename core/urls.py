from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('fanlar/', fanlar_view),
    path('fanlar/<int:fan_id>/delete/', fan_delete_view),
    path('fanlar/<int:fan_id>/update/', fan_update_view),
    path('yonalishlar/', yonalishlar_view),
    path('yonalishlar/<int:yonalish_id>/delete/', yonalish_delete_view),
    path('yonalishlar/<int:yonalish_id>/delete/confirm/', yonalish_delete_confirm_view),
    path('yonalishlar/<int:yonalish_id>/update/', yonalish_update_view),

    path('ustozlar/', ustozlar_view),
    path('ustozlar/<int:ustoz_id>/delete/', ustoz_delete_view),
    path('ustozlar/<int:ustoz_id>/update/', ustozlar_update_view),
]
