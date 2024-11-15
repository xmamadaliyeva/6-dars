from django.contrib import admin
from .models import *
# Register your models here.

#class NewAdmin(admin.ModelAdmin):
 #   list_display = ('title','text','date','author')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(News)