from django.conf.urls import patterns, include, url
import main.views as views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^recur/$', views.RecurItemView.as_view()),
                       url(r'^cash/$', views.CashView.as_view()),
    # Examples:
    # url(r'^$', 'cashflow.views.home', name='home'),
    # url(r'^cashflow/', include('cashflow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
