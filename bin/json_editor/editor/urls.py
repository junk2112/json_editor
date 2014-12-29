from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'editor.views.home'),
    # url(r'/editor/^$', 'editor.views.editor'),
)
