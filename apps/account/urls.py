from django.conf.urls import url

from account import views

urlpatterns = [
    url('register/', views.register, name='register'),
    url('update/', views.update),
    url('login/', views.login_view, name='login'),
    url('logout/', views.logout_view, name='logout'),
    url('mail/', views.hello_mail),
    url('active/', views.active_account),
]
