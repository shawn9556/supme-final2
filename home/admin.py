from django.contrib import admin
from home.models import PotentialUser
# Register your models here.

class PotenUserAdmin(admin.ModelAdmin):
    list_display = ["id", "poten_user_email"]

admin.site.register(PotentialUser, PotenUserAdmin)