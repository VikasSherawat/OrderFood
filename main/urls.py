from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^shopowner/', include('main.ShopOwner.urls')),
    url(r'^customer/', include('main.Customer.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^success/$', views.success, name='success'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
