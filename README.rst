django facebook auth helper
===========================
Facebook auth login library based on Django
class based structure

A stable for Django >= 1.7 & Python >= 2.7

Configuration
-------------
Settings
''''''''
0. Install django_facebook_auth_helper
   ::

       pip install django_facebook_auth_helper

1. Add django_facebook_auth to INSTALLED_APPS
   ::

       INSTALLED_APPS = (
           'django_facebook_auth',
       )

2. Add authentication backends to AUTHENTICATION_BACKENDS
   ::

      AUTHENTICATION_BACKENDS = (
          'django_facebook_auth.backends.FacebookBackend',
      )

3. Add facebook settings to settings.py
   ::

       FACEBOOK_APP_ID = YOUR_APP_ID
       FACEBOOK_APP_SECRET = 'YOUR_APP_SECRET'
       FACEBOOK_REDIRECT_URI = 'http://localhost:8000/login/'

4. Import django_facebook_auth modules to views.py
   ::

       from django_facebook_auth.views import FacebookLoginMixin
       from django_facebook_auth.models import FacebookSession
