from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',                      # edited
         views.post_detail,                                                    # new
         name='post_detail'),                                                  # new

]
