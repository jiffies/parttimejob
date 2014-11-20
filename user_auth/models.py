#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_delete
import os.path

# Create your models here.
class User_extra(models.Model):
    user = models.OneToOneField(User,verbose_name="用户")
    mobile_number = models.CharField("手机号码",max_length=20)
    province= models.CharField("省",max_length=30,blank=True)  #省
    city = models.CharField("市",max_length=30,blank=True)     #市
    county = models.CharField("区县",max_length=30,blank=True)   #县区
    commercial_district = models.CharField("商圈",max_length=30,blank=True) #商圈
    identity_card_number = models.CharField("身份证号码",max_length=30,blank=True)#身份证号
    identity_card_image = models.ImageField("上传手持身份证照片",upload_to='identity_card',blank=True)


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
    user = models.OneToOneField(User,verbose_name="用户")
    real_name = models.CharField("真实姓名",max_length=30)
    sex = models.CharField("性别",max_length=1,choices=SEX) 
    birthday = models.DateField("出生日期")
    workon = models.CharField("身份",max_length='30',choices=WORK)#从事工作


class Corporation_profile(models.Model):
    user = models.OneToOneField(User,verbose_name="用户")
    corporation_name = models.CharField("商户名称",max_length=30,blank=True)#商户名称
    business_license = models.CharField("营业执照编号",max_length=50,blank=True)#营业执照编号
    business_license_image = models.ImageField("上传营业执照图片",upload_to='business_license',blank=True)

import os
import os.path
from django.conf import settings
from functools import partial
#need refactor
def delete_file(attrname,sender,**kwargs):
    print "##########~~~~~~~~~~~~~~~~~"
    instance = kwargs['instance']
    print getattr(instance,attrname).path
    try:
        os.remove(os.path.join(settings.BASE_DIR,getattr(instance,attrname).path))
    except:
        pass
        


post_delete.connect(partial(delete_file,'identity_card_image'),User_extra,weak=False)#,attr='identity_card_image')
post_delete.connect(partial(delete_file,'business_license_image'),sender=Corporation_profile,weak=False)
