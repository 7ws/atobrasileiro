from django.conf.urls import patterns, url

from hotsite.views import MainView


urlpatterns = patterns(
    '',

    url(r'^$', MainView.as_view(), name='home'),
)
