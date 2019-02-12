from django.conf.urls import url
from .views import *

app_name = 'post'

urlpatterns = [
    url(r'^index/', post_index, name='index'),
    url(r'^detail/(?P<postId>\d+)/', post_detail, name='detail'),
    url(r'^create/', post_create, name='create'),
    url(r'^update/(?P<id>\d+)/', post_update, name='update'),
    url(r'^delete/(?P<id>\d+)/', post_delete, name='delete'),
]