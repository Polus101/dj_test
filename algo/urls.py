from django.urls import path
from . import views

urlpatterns = [
    path('', views.new),
    path('new', views.new),
    path('view', views.view),
    path('filters', views.filters),
]
