from django.urls import path

from . import views 

urlpatterns = [
    path('', views.detail, name='schedule'),
    
    path('event/create', views.EventCreateView.as_view(), name='event_create'),
    path('event/read/<int:pk>', views.EventReadView.as_view(), name='event_read'),
    path('event/update/<int:pk>', views.EventUpdateView.as_view(), name='event_update'),
    path('event/delete/<int:pk>', views.EventDeleteView.as_view(), name='event_delete'),
    path('event/', views.EventList.as_view(), name='event_list'), 

    path('visit/create', views.VisitCreateView.as_view(), name='visit_create'),
    path('visit/read/<int:pk>', views.VisitReadView.as_view(), name='visit_read'),
    path('visit/update/<int:pk>', views.VisitUpdateView.as_view(), name='visit_update'),
    path('visit/delete/<int:pk>', views.VisitDeleteView.as_view(), name='visit_delete'),
    path('visit/', views.VisitList.as_view(), name='visit_list'), 

]