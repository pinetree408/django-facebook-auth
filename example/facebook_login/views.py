from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from django.views.generic import View, TemplateView

from django_facebook_auth.views import FacebookLoginMixin
from django_facebook_auth.models import FacebookSession


class ExampleUserDetail(TemplateView):
    template_name = "example_user_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ExampleUserDetail, self).get_context_data(**kwargs)
        facebook_session = FacebookSession.objects.get(user_id=self.request.user.pk)
        user = facebook_session.user
        profile = facebook_session.query('me')

        context['username'] = user.username
        context['facebookid'] = profile['id']

        return context


class ExampleLogin(FacebookLoginMixin, View):
    template_name = "example_login.html"


class ExampleLogout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
