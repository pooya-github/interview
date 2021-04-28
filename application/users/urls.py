from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('', views.search, name='search'),
    path('answer', views.searchResult, name='searchResult'),
]