from django.urls import path

from . import views 

urlpatterns = [
    path('<slug:pk>/', views.EventDetailView.as_view()),
]