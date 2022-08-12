from django.urls import path, include
from django.contrib.auth import views as auth_views                            # new
from . import views

urlpatterns = [
    # previous login view                                                        new
    # path('login/', views.user_login, name='login'),                            edited
    # login / logout urls                                                        new
    path('login/', auth_views.LoginView.as_view(), name='login'),              # new
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),           # new
]
