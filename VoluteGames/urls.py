from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VoluteGames.views.home', name='home'),
    # url(r'^VoluteGames/', include('VoluteGames.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'news.views.index'),
	url(r'^home$', 'news.views.index'),
	url(r'^auth$', 'VoluteGames.views.authorization'),
	url(r'^login$', 'VoluteGames.views.login'),
	url(r'^logout$', 'VoluteGames.views.logout'),
	url(r'^reg$', 'VoluteGames.views.registration'),
	url(r'^signup$', 'VoluteGames.views.signup'),
)

urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
)