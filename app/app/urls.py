from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from demo.views import DemoUserDetail, DemoLogin, DemoLogout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_Facebook_Auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(DemoUserDetail.as_view()), name='index'),
    url(r'^login/', DemoLogin.as_view(), name='login'),
    url(r'^logout/', DemoLogout.as_view(), name='logout_page'),
)
