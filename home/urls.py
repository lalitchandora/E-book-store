from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home-page'),
    path('profile/', views.profile, name = 'profile'),
    path('genre/<str:genretype>',views.genre_search,name = 'genre_search'),
]