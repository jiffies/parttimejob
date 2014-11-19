#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_delete
import os.path

# Create your models here.
class User_extra(models.Model):
    user = models.OneToOneField(User)
    mobile_number = models.CharField(max_length=20)
    province= models.CharField(max_length=30,blank=True)  #省
    city = models.CharField(max_length=30,blank=True)     #市
    county = models.CharField(max_length=30,blank=True)   #县区
    commercial_district = models.CharField(max_length=30,blank=True) #商圈
    identity_card_number = models.CharField(max_length=30,blank=True)#身份证号
    identity_card_image = models.ImageField(upload_to='identity_card',blank=True)


class Employee_profile(models.Model):
    SEX = (
        ('M','男性'),
        ('F','女性'),
    )
    WORK = (
        ('student','学生'),
        ('working','在职'),
        ('work at home','自由职业者'),
        ('other','其他'),
    )
    user = models.OneToOneField(User)
    real_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1,choices=SEX) 
    birthday = models.DateField()
    workon = models.CharField(max_length='30',choices=WORK)#从事工作


class Corporation_profile(models.Model):
    user = models.OneToOneField(User)
    corporation_name = models.CharField(max_length=30,blank=True)#商户名称
    business_license = models.CharField(max_length=50,blank=True)#营业执照编号
    business_license_image = models.ImageField(upload_to='business_license',blank=True)

import os
import os.path
from django.conf import settings
#need refactor
def delete_file(sender,**kwargs):
    instance = kwargs['instance']
    if sender is User_extra:
        try:
            os.remove(os.path.join(settings.BASE_DIR,instance.identity_card_image.path))
        except:
            pass
    elif sender is Corporation_profile:
        try:
            os.remove(os.path.join(settings.BASE_DIR,instance.business_license_image.path))
        except:
            pass


post_delete.connect(delete_file,User_extra)#,attr='identity_card_image')
post_delete.connect(delete_file,sender=Corporation_profile)
