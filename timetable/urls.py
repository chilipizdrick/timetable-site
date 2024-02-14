from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('timetable/', views.timetable, name='timetable'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('manage_profile/', views.manage_profile, name='manage_profile'),
]
