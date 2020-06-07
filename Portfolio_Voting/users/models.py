from django.db import models

# Create your models here.
class User(models.Model):
	studID = models.CharField(max_length=200)
	fullName = models.CharField(max_length=200)
	department = models.CharField(max_length=200)
	choice_text = models.CharField(max_length=200)

	def __str__(self):
		return self.fullName

'''
studID			帳號 (學號)
fullName		姓名
department		系所
choice_text		所投票的作品名稱
'''