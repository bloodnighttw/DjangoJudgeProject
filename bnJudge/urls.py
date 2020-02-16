from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from bnJudge.view import index
from accounts.views import register,login,logout
from repo import views as repoViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',index),
    path('signup/', register, name='register'),
    path('login/', login),
    path('logout/',logout),
    path('<str:id>/',repoViews.test),
    

]
