from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ('id','ism')
    list_display = ("id","ism", "jins", "kitob_soni")
    list_display_links = ("ism",'jins')
    list_editable = ('kitob_soni',)
    list_filter = ('jins',)
    list_per_page = 7
    # list_max_show_all = 1000

@admin.register(Record)
class RecordAdmin(ModelAdmin):
    search_fields = ('id', 'student__ism', 'kitob__nom')
    autocomplete_fields = ("student",)

admin.site.register(Muallif)
admin.site.register(Kitob)




