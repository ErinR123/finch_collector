from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'), # `name='home'` kwarg gives the route a name - naming is optional, but good practice (it will come in handy later)
 path('about/', views.about, name='about'),
 path('finches/', views.finches_index, name='index'),
]

