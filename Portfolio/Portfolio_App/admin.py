from django.contrib import admin
from Portfolio_App.models import Response_m
# Register your models here.
class Response_mAdmin(admin.ModelAdmin):
    list_display = ['name','email','comment']
admin.site.register(Response_m,Response_mAdmin)
