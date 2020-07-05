from django.db import models

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from polls.models import Choice

# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, studID, fullName, department, is_active, is_admin, password):
		"""
		Creates and saves a User with the given studID and password.
		"""
		if not studID:
			raise ValueError("ENTER AN EMAIL BUDDY")
		if not fullName:
			raise ValueError("I KNOW YOU HAVE A NAME")
		if not department:
			raise ValueError("department???")
		if not password:
			raise ValueError("PASSWORD?!?!?!? HELLO??")

		user = self.model(
			studID=studID,
			fullName=fullName,
			department=department,
			is_active=is_active,
			is_admin=is_admin,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, studID, fullName, department, is_active, is_admin, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
			studID=studID,
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
	
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	studID = models.CharField(verbose_name='學號', max_length=200, unique=True)
	fullName = models.CharField(verbose_name='中文全名', max_length=200)
	department = models.CharField(verbose_name='系所', max_length=200)
	is_active = models.BooleanField(verbose_name='啟用', default=True)
	is_admin = models.BooleanField(verbose_name='管理員', default=False)

	objects = UserManager()

	USERNAME_FIELD = 'studID'
	REQUIRED_FIELDS = ['fullName', 'department', 'is_active', 'is_admin']
	

	def __str__(self):
		# return self.fullName
		return "@{}: {}".format(self.fullName, self.studID)


	def has_perm(self, perm, obj=None):
		return True #is_superuser self.is_admin

	def has_module_perms(self, app_label):
		return True #is_superuser self.is_admin

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

'''
studID			帳號 (學號)
fullName		姓名
department		系所
choice_text		所投票的作品名稱

'''

class User_Vote(models.Model):
    choice_text = models.ForeignKey("polls.Choice", on_delete=models.CASCADE)
    studID = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text