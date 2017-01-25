from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from models import FacebookSession
from django.conf import settings
import cgi
import urllib


class FacebookLoginMixin(object):
    template_name = "login.html"
    login_settings = settings
    redirect_path = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.redirect_path)
	return super(FacebookLoginMixin, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if 'code' in request.GET:
            args = {
                'client_id': settings.FACEBOOK_APP_ID,
                'redirect_uri': settings.FACEBOOK_REDIRECT_URI,
                'client_secret': settings.FACEBOOK_APP_SECRET,
                'code': request.GET['code']
            }
            url = 'https://graph.facebook.com/oauth/access_token?'
            url = url + urllib.urlencode(args)
            response = cgi.parse_qs(urllib.urlopen(url).read())
            access_token = response['access_token'][0]
            expires = response['expires'][0]

	    facebook_session = FacebookSession.objects.get_or_create(access_token=access_token)[0]
            facebook_session.expires = expires
            facebook_session.save()
            user = auth.authenticate(token=access_token)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(self.redirect_path)

	context = {
	    'settings': self.login_settings
	}
        return render(request, self.template_name, context)
