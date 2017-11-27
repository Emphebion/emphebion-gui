from django.conf.urls import url

from . import views

app_name = 'stones'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<stone_id>[0-9]+)/$', views.stone_detail, name='stone_detail'),
    url(r'^(?P<stone_id>[0-9]+)/mod_access/$', views.stone_mod_access, name='stone_mod_access'),
]

