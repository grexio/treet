from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'core.views.home', name='home'),
                       url(r'^add-treet/$', 'market.views.new_treet', name='new-treet'),
                       url(r'^treet/(?P<treet_id>[0-9]+)/$', 'market.views.treet_details', name='treet-details'),
                       url(r'^admin/', include(admin.site.urls)),
                       ) + static(settings.STATIC_URL,
                                  document_root=settings.STATIC_ROOT)
