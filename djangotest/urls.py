from django.conf.urls import patterns, include, url

from django.contrib import admin

import contacts.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', contacts.views.ListContactView.as_view(),
        name='contacts-list'),
    url(r'^new$', contacts.views.CreateContactView.as_view(),
    		name='contacts-new'),
)
