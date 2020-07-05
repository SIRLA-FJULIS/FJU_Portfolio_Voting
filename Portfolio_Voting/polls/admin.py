from django.contrib import admin
from .models import Choice, Question

# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)