from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    # login / logout urls
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # change password urls
    path('password-change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/',
       auth_views.PasswordChangeDoneView.as_view(),
       name='password_change_done'),

    # reset password urls                                                        new
    path('password-reset/',                                                    # new
         auth_views.PasswordResetView.as_view(),                               # new
         name='password_reset'),                                               # new
    path('password-reset/done/',                                               # new
         auth_views.PasswordResetDoneView.as_view(),                           # new
         name='password_reset_done'),                                          # new
    path('password-reset/<uidb64>/<token>/',                                   # new
         auth_views.PasswordResetConfirmView.as_view(),                        # new
         name='password_reset_confirm'),                                       # new
    path('password-reset/complete/',                                           # new
         auth_views.PasswordResetCompleteView.as_view(),                       # new
         name='password_reset_complete'),                                      # new

    path('', views.dashboard, name='dashboard'),

]
