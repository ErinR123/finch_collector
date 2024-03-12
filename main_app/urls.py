from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'), # `name='home'` kwarg gives the route a name - naming is optional, but good practice (it will come in handy later)
 path('about/', views.about, name='about'),
 path('finches/', views.finches_index, name='index'),
 path('finches/<int:finch_id>/', views.finches_details, name='details'),
 path('finches/create', views.FinchCreate.as_view(), name='finches_create'),
 path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
 path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
 path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]

