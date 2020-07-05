from django.contrib import admin

from portfolios.models import Work

# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'thumbnail', 'pdf_file', 'created_date')

admin.site.register(Work, WorkAdmin)