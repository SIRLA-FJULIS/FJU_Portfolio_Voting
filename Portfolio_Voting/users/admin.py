from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_admin', 'fullName', 'department')

admin.site.register(User, UserAdmin)