
from django.urls import path
from .import views


urlpatterns = [
    
    path('',views.index,name ='index'),
    path('songs/',views.songs,name='songs'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('songs/<int:id>/',views.songpost,name='songpost'),
    path('watchlater/',views.watchlater,name='watchlater'),
     path('logout_user', views.logout_user, name='logout_user'),


] 
