from django.contrib import admin
from django.urls import path
from Medico import views

urlpatterns = [
    path('',views.Home, name='Home'),
    path('signup/',views.Signup, name='signup'),
    path('login/',views.Login, name='login'),
    path('admin/', admin.site.urls),
]
