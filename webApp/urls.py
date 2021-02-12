from django.conf.urls import url
from webApp import views
app_name='webApp'
urlpatterns = [
    url(r'^os/$',views.operatingSystem,name='operatingSystem'),
    url(r'^browser/$',views.browser,name='browser'),
    url(r'^country/$',views.country,name='country'),
    url(r'^time/$',views.times,name='times'),
    url(r'^search/$',views.search,name='search'),
]