from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.superadmin_dashboard,name='superadmin_dashboard'),

    path('logout/', auth_views.LogoutView.as_view(), name='superadmin_dashboard_logout'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/userLogin.html'), name='login'),


]