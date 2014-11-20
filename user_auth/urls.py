from django.conf.urls import patterns,url,include
from user_auth import views

urlpatterns = patterns('',
    url(r'^login/$','django.contrib.auth.views.login',name='login'),        
)
