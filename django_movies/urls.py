from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url('home/', include('home.urls')),
    url('account/', include('account.urls')),
]
