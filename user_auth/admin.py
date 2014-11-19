from django.contrib import admin
from user_auth.models import Employee_profile,Corporation_profile,User_extra

# Register your models here.
admin.site.register(User_extra)
admin.site.register(Employee_profile)
admin.site.register(Corporation_profile)
