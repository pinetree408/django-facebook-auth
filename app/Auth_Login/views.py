from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from models import FacebookSession
from django.conf import settings
import cgi
import urllib


@login_required
def index(request):
    facebook_session = FacebookSession.objects.get(user_id=request.user.pk)
    user = facebook_session.user
    profile = facebook_session.query('me')
    context = {
        'username': user.username,
        'facebookid': profile['id']
    }

    return render(request, 'index.html', context)


def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.GET:

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
                    return HttpResponseRedirect('/')

    context = {
        'settings': settings
    }

    return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
