from django.db import models
from django.utils import timezone

# Create your models here.
class Work(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	description = models.TextField()
	thumbnail = models.ImageField(upload_to='thumbnail', blank=True)
	pdf_file = models.FileField(upload_to='pdf_file', blank=True)
	video_url = models.URLField(max_length=200, blank=True)
	created_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-created_date',)

	def __str__(self):
		return self.title

'''
title			作品名稱
author			作者
description		作品描述
thumbnail		作品縮圖
pdf_file 		pdf檔案附件
video_url 		youtube檔案連結
created_date	發布時間
'''

# 投票 (參考網站)
# https://keydocsdjango.readthedocs.io/en/latest/Django%E5%88%9B%E5%BB%BA%E6%8A%95%E7%A5%A8app%E5%BF%AB%E9%80%9F%E9%A2%84%E8%A7%88.html