from django.conf.urls import patterns, include, url

from django.contrib import admin
from app01.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^$',index),
    (r'^account_login/',account_login),
    (r'^logout/$',logout),
    (r'^dashboard/$',dashboard),
    (r'^auto/$',auto),
)
