from django.contrib import admin

from .models import *

# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class CountyType1Admin(admin.ModelAdmin):
    list_display = ('name', 'id')

class CountyType2Admin(admin.ModelAdmin):
    list_display = ('name', 'id')

class CountyType3Admin(admin.ModelAdmin):
    list_display = ('name', 'id')

class GroupType1County3Admin(admin.ModelAdmin):
    list_display = ('name', 'id')

class GroupType2County3Admin(admin.ModelAdmin):
    list_display = ('name', 'id')

class GroupType3County1Admin(admin.ModelAdmin):
    list_display = ('name', 'id')





admin.site.register(TypeCategory, TypeAdmin)
admin.site.register(CountyType1, CountyType1Admin)
admin.site.register(CountyType2, CountyType1Admin)
admin.site.register(CountyType3, CountyType1Admin)
admin.site.register(GroupType1County3, GroupType1County3Admin)
admin.site.register(GroupType2County3, GroupType2County3Admin)
admin.site.register(GroupType3County1, GroupType3County1Admin)
admin.site.register(Kamisama)
admin.site.register(God)

admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Work)

admin.site.register(TaggedItem)