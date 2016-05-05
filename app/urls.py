from django.conf.urls import url
from django.contrib import admin
from . import views

admin.autodiscover()


urlpatterns = [
    url(r'^post/(?P<pk>[0-9]+)/map/$', views.post_map, name='post_map'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post_user/(?P<pk>[0-9]+)/$', views.post_detail_user, name='post_detail_user'),
    url(r'^post/new_user/$', views.post_new_user, name='post_new_user'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post_user/(?P<pk>[0-9]+)/edit/$', views.post_edit_user, name='post_edit_user'),
    # url(r'^drafts/(\d+)/$', views.post_draft_list, name='post_draft_list'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^drafts_user/$', views.post_draft_list_user, name='post_draft_list_user'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post_user/(?P<pk>[0-9]+)/publish/$', views.post_publish_user, name='post_publish_user'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post_user/(?P<pk>\d+)/remove/$', views.post_remove_user, name='post_remove_user'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment_user/(?P<pk>\d+)/approve/$', views.comment_approve_user, name='comment_approve_user'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^comment_user/(?P<pk>\d+)/remove/$', views.comment_remove_user, name='comment_remove_user'),
    # url(r'^comment/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^auth/register/$', views.register, name='register'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^page/(\d+)/$', views.post_list, name='post_list'),
    url(r'^page_user/(\d+)/$', views.post_list_user, name='post_list_user'),
    url(r'^page_user/$', views.post_list_user, name='post_list_user'),
    url(r'^', views.post_list, name='post_list'),
]