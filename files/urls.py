from django.urls import path
from . import views

urlpatterns = [
    path("files/",views.FilesView.as_view()), 
    # path("categories/", views.CategoryCreateView.as_view()),    
    # path("categories/<str:pk>/", views.CategoryDetailView.as_view()),   
]