from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shopowner/', include('main.ShopOwner.urls')),
]
