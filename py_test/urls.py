from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.huindex, name='huindex'),
    url(r'^index/', include('index.urls')),
    url(r'^admin/', admin.site.urls),
]