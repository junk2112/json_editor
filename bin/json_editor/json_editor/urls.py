from django.conf.urls import patterns, include, url
from django.contrib import admin
import editor
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'json_editor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('editor.urls')),
)
