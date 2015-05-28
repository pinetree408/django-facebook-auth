from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_Facebook_Auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Auth_Login.views.index', name='index'),
    url(r'^login/', 'Auth_Login.views.login', name='login'),
    url(r'^logout/', 'Auth_Login.views.logout_page', name='logout_page'),
)
