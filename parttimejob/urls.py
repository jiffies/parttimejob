from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'parttimejob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/',include('user_auth.urls',namespace='auth')),
    url(r'^api/v1/register/$','user_auth.views.user_register',name='register'),
    url(r'^api/v1/token-auth/$', views.obtain_auth_token),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
