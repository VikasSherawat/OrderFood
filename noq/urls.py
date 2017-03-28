from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('main.urls')),  # this line added
    url(r'^admin/', admin.site.urls),
]
