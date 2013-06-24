from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('hotsite.urls')),

) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
    show_indexes=True)


# Unregister sites from Admin
from django.contrib.sites.models import Site
admin.site.unregister(Site)
