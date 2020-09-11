from django.contrib import admin
from .models import User, Visitor_Infos

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_admin', 'fullName', 'department')

admin.site.register(User, UserAdmin)


class Visitor_InfosAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'page_visited', 'event_date')

admin.site.register( Visitor_Infos,  Visitor_InfosAdmin)
