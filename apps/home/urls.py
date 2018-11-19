from django.conf.urls import url

from apps.home import views

urlpatterns = [
    url(r'detail/(\d+)', views.detail,name='detail')
]
