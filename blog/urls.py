from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^createpost/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<post_pk>\d+)/commentcreate/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comment/(?P<comment_pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),



]
