from django.contrib import admin

from portfolios.models import Work, UserVote

# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'work_college', 'work_department', 'pdf_file', 'created_date')

class UserVoteAdmin(admin.ModelAdmin):
	list_display = ('studID', 'choice_workTitle')

admin.site.register(Work, WorkAdmin)
admin.site.register(UserVote, UserVoteAdmin)