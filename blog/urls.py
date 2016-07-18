from django.conf.urls import url, include
from blog.views import PostsListView, post_detail_func_view

urlpatterns = [
    url(r'^$',PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',post_detail_func_view, name='detail'),
    url(r'^login','django.contrib.auth.views.login',{'redirect_field_name':'/'})
]
