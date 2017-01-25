django facebook auth helper
===========================
Facebook auth login library based on Django
class based structure

A stable for Django >= 1.7 & Python >= 2.7

Configuration
-------------
Settings
''''''''
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

       FACEBOOK_APP_ID = 704150899695055
       FACEBOOK_APP_SECRET = '6632df15dddaafb2a65043f1b0871655'
       FACEBOOK_REDIRECT_URI = 'http://localhost:8000/login/'
