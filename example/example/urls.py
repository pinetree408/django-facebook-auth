from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from facebook_login.views import ExampleUserDetail, ExampleLogin, ExampleLogout

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Facebook login urls
    url(r'^$', login_required(ExampleUserDetail.as_view()), name='user_detail'),
    url(r'^login/', ExampleLogin.as_view(), name='login'),
    url(r'^logout/', ExampleLogout.as_view(), name='logout_page'),
)
