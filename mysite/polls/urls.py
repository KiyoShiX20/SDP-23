
#from django.urls import path

#from . import views

#urlpatterns = [
  #  path("", views.home, name = "home"),
   # path('students', views.students , name = "students"),
   #path("time/", views.time, name = "home"),
    #path("template_view/", views.template_view, name = "home"),
    #path("register/", views.register, name = "register"),
    #path("login/", views.login, name = "login")
#]

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', include('first.urls')),
]

"""
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', include('first.urls')),
]
"""
from django.urls import path
from polls import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),

]