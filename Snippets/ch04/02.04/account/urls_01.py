from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    # login / logout urls
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # change password urls                                                       new
    path('password-change/',                                                   # new
         auth_views.PasswordChangeView.as_view(),                              # new
         name='password_change'),                                              # new
    path('password-change/done/',                                              # new
          auth_views.PasswordChangeDoneView.as_view(),                         # new
          name='password_change_done'),                                        # new

    path('', views.dashboard, name='dashboard'),

]
