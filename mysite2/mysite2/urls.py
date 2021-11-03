from django.conf.urls import url
from django.urls import path
from register.views import register
from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path("home/", views.home, name='home'),
    path("", views.home, name='home'),
    path("create/", views.create, name='create'),
    path("register/", register, name='register'),
    path("view/",views.view,name="view")
]
