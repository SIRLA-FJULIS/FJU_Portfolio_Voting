from django.contrib import admin
from .models import User, User_Vote

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('studID', 'is_active', 'is_admin', 'fullName', 'department')

class User_VoteAdmin(admin.ModelAdmin):
	list_display = ('studID', 'choice_text')

admin.site.register(User, UserAdmin)
admin.site.register(User_Vote, User_VoteAdmin)