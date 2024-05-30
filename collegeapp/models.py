from typing import Any
from django.db import models
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin

class Department(models.Model):
    department=models.CharField(max_length=30)
    batch=models.CharField(max_length=20)

class Teacher (models.Model):
    t_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    

class Student (models.Model):
    roll_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)
    email=models.EmailField(unique=True)
    batch=models.CharField(max_length=30)
    TEACHER = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Subject(models.Model):
    name=models.CharField(max_length=20)
    code=models.CharField(max_length=20,unique=True)
    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE)

class Marks(models.Model):
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    TEACHER=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    marks=models.IntegerField()


class CustomUser(UserManager):
    def create_user(self, email, password, **extra_fields) :
        if not email:
            raise ValueError("you have entered incorrect email")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user
    
    def create_superuser(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)   
        return self.create_user(email,password,**extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
     email=models.EmailField(default='',unique=True)
     name=models.CharField(max_length=255,blank=True,default='')


     is_active=models.BooleanField(default=True)
     is_superuser=models.BooleanField(default=False)
     is_staff=models.BooleanField(default=False)
     is_supersuperuser=models.BooleanField(default=False)


     objects=CustomUser()

     USERNAME_FIELD='email'
     EMAIL_FIELD='email'
     REQUIRED_FIELDS=[]


   
 

