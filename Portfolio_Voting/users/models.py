from django.db import models

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, username, fullName, department, is_active, is_admin, password):

		if not fullName:
			raise ValueError("Please enter your fullName.")
		if not department:
			raise ValueError("Please enter your department.")

		user = self.model(
			username=username,
			fullName=fullName,
			department=department,
			is_active=is_active,
			is_admin=is_admin,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, fullName, department, is_active, is_admin, password):

		user = self.create_user(
			username=username,
			fullName=fullName,
			department=department,
			password=password,
			is_active=is_active,
			is_admin=is_admin,
		)
		user.save(using=self._db)
		return user

# hook in the New Manager to our Model
class User(AbstractBaseUser):
	username = models.CharField(max_length=40, unique=True)
	fullName = models.CharField(verbose_name='中文全名', max_length=200, blank=True)
	department = models.CharField(verbose_name='系所', max_length=200, blank=True)
	is_active = models.BooleanField(verbose_name='啟用', default=True)
	is_admin = models.BooleanField(verbose_name='管理員', default=False)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['is_active', 'is_admin']
	

	def __str__(self):
		return "@{}".format(self.username)

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		# "Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

'''
username		帳號 (學號)
fullName		中文全名
department		系所
is_active		啟用
is_admin		管理員
'''