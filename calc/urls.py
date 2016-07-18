from django.conf.urls import url
from calc import views

urlpatterns = [
    url(r'^$',views.calculate,name='calc'),
]
