from django.contrib import admin
from mypage.models import Profile, Select
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'for_user']
admin.site.register(Profile, ProfileAdmin)

class SelectAdmin(admin.ModelAdmin):
    list_display = ['id', 'selector','selection_state', 'create_date']
admin.site.register(Select, SelectAdmin)