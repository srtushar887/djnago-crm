from django.urls import path

from . import views

urlpatterns=[
    path('',views.user_login_page,name='user_login_page'),
    # path('register/',views.user_login_register,name='user_login_register'),
]