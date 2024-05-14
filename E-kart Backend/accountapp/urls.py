from django.urls import path
from accountapp import views
urlpatterns = [
    path('login',views.user_login),
    path('register',views.user_register),
    path('logout',views.user_logout),

]