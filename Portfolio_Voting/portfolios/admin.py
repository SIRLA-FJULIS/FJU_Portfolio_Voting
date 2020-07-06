from django.contrib import admin

from portfolios.models import Work, User_Vote

# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'work_management', 'work_department', 'pdf_file', 'created_date')

class User_VoteAdmin(admin.ModelAdmin):
	list_display = ('studID', 'choiceText_workTitle', 'votes')

admin.site.register(Work, WorkAdmin)
admin.site.register(User_Vote, User_VoteAdmin)