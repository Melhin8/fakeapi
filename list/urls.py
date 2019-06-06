from django.conf.urls import url

from . import views
app_name = 'elfs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^add/$', views.add, name='add'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='detail'),
]