from django.conf.urls import url, include
from django.contrib import admin

from home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.index),
    url('home/', include('home.urls')),
    url('account/', include('account.urls')),
]
