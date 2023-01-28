from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('search/', views.getSearchResults, name='search-results'),
]

