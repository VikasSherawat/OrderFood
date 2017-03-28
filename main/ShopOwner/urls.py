from django.conf.urls import url
from . import views

app_name = 'shopowner'
urlpatterns = [
    # ex: /noq/shopowner/
    url(r'^$', views.index, name='index'),
    # ex: /noq/shopowner/5/
    url(r'^(?P<shop_id>[0-9]+)/$', views.shop, name='shop'),
    # ex: /noq/shopowner/newshop/
    url(r'^newshop/$', views.newshop, name='newshop'),
]
