from django.conf.urls import url
from blog.views import PostsListView, post_detail_func_view

urlpatterns = [
    url(r'^$',PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',post_detail_func_view, name='detail'),
] 
