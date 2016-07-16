from django.conf.urls import url
from blog.views import PostsListView, post_detail_func_view, logout_page, login_page
from django.contrib.auth import views

urlpatterns = [
    url(r'^$',PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',post_detail_func_view, name='detail'),
    url(r'^login$', login_page,name="login_p"),
    url(r'^logout$', logout_page,name="logout_p")
]
