from django.contrib import admin

from portfolios.models import Work

# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'file', 'created_date') #like

admin.site.register(Work, WorkAdmin)