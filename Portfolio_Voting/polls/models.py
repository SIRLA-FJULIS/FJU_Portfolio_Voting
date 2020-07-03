from django.db import models
from django.utils import timezone
import datetime

from portfolios.models import Work

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now >= self.pub_date >= now - datetime.timedelta(days=1)
		
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	list_filter = ['pub_date']
	search_fields = ['question_text']

class Choice(models.Model):
	question = models.ForeignKey("polls.Question", on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	# choice_text = models.ForeignKey("portfolios.Work", on_delete=models.CASCADE) #https://iter01.com/418588.html
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text

'''
class Question:
	question_text	投票主題(問題)
	pub_date		開始投票的日期

class Choice:
	question 		投票主題(問題)
	choice_text		投票的選項
	votes			票數
'''