from django.contrib import admin
from .models import *

# Register your models here.

class restaurant_(admin.ModelAdmin):
    list_display=('name','image')

admin.site.register(Restaurant,restaurant_)

class register_(admin.ModelAdmin):
    list_display=['name','email','contact','address','password']
    list_filter=['email','name','password']
    search_fields=['name']

admin.site.register(Register,register_)

class logo_(admin.ModelAdmin):
    list_display=['name','logo']

admin.site.register(Logo,logo_)
