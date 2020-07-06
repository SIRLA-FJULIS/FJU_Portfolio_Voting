from django.db import models
from django.utils import timezone

# Create your models here.
MANAGEMENT_CHOICES = (
    ("文學院", "文學院"),
    ("藝術學院", "藝術學院"),
    ("傳播學院", "傳播學院"),
    ("教育學院", "教育學院"),
    ("醫學院", "醫學院"),
    ("理工學院", "理工學院"),
    ("外國語文學院", "外國語文學院"),
    ("民生學院", "民生學院"),
    ("法律學院", "法律學院"),
	("社會科學院", "社會科學院"),
	("管理學院", "管理學院"),
	("織品服裝學院", "織品服裝學院"),
)

class Work(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	work_management = models.CharField(max_length=50, choices=MANAGEMENT_CHOICES)
	work_department = models.CharField(max_length=200)
	description = models.TextField()
	pdf_file = models.FileField(upload_to='pdf_file', blank=True)
	video_url = models.URLField(max_length=200, blank=True)
	created_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-created_date',)

	def __str__(self):
		return self.title

class User_Vote(models.Model):
	choiceText_workTitle = models.ForeignKey("portfolios.Work", on_delete=models.CASCADE)
	studID = models.CharField(max_length=200, unique=True, blank=False)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.studID

	# class Meta:
 #        get_latest_by = 'choiceText_workTitle'

'''
Work
	title			作品名稱
	author			作者
	work_management	作者之所屬學院
	work_department	作者之所屬系所
	description		作品描述
	pdf_file 		pdf檔案附件
	video_url 		youtube檔案連結
	created_date	發布時間

Choice
	choiceText_workTitle	被投票的作品名稱
	studID					投票者
	votes					票數
'''

# 投票 (參考網站)
# https://keydocsdjango.readthedocs.io/en/latest/Django%E5%88%9B%E5%BB%BA%E6%8A%95%E7%A5%A8app%E5%BF%AB%E9%80%9F%E9%A2%84%E8%A7%88.html