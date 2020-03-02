from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^today/$',views.album_of_day,name='albumToday')
]