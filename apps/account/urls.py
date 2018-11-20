from django.conf.urls import url

from account import views

urlpatterns = [
    url('register/', views.register),
    url('update/', views.update),
    url('login/', views.login_view),
    url('logout/', views.logout_view),
]
