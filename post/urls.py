from django.conf.urls import url
from .views import *

app_name = 'post'

urlpatterns = [
    url(r'^index/', post_index, name='index'),
    url(r'^create/', post_create, name='create'),
    url(r'^detail/(?P<slug>[\w-]+)/', post_detail, name='detail'),
    url(r'^update/(?P<slug>[\w-]+)/', post_update, name='update'),
    url(r'^delete/(?P<slug>[\w-]+)/', post_delete, name='delete'),
]