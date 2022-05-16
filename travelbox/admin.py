from django.contrib import admin
from travelbox.models import *

# Register your models here.

class Travel_BoxAdmin(admin.ModelAdmin):
    list_display = ['id', 'travel_box_user', 'create_date']
admin.site.register(Travel_box, Travel_BoxAdmin)
admin.site.register(GetPic)