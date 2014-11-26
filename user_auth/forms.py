#! coding:utf-8
from django.forms import widgets
from user_auth.models import User_extra,Corporation_profile,Employee_profile
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="密码",widget=widgets.PasswordInput())
    repeatpassword = forms.CharField(label="请再次输入密码",widget=widgets.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')
        labels = {
            'username':"用户名",
            'password':"密码",
            'repeatpassword':"请再次输入密码",
        }
        help_texts = {
            'username':''        
        }

    #def clean_repeatpassword(self):
        #print self.cleaned_data
        #repeatpassword = self.cleaned_data['repeatpassword']
        #password = self.cleaned_data.get('password')
        #if repeatpassword != password:
            #raise forms.ValidationError("密码不一致，请重新输入。")
        #return repeatpassword
        
