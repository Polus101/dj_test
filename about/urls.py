from django.urls import path
from . import views

urlpatterns = [
    path('', views.me),
    path('me', views.me),
    path('op', views.op),
    path('managers', views.managers),
    path('classmates', views.classmates)
]
