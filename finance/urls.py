from django.urls import path

from . import views 

urlpatterns = [
    path('Costcenter/<slug:pk>/', views.CostcenterDetailView.as_view()),
    path('', views.detail, name="detail"),

    path('expense/create', views.ExpenseCreateView.as_view(), name='expense_create'),
    path('expense/read/<int:pk>', views.ExpenseReadView.as_view(), name='expense_read'),
    path('expense/update/<int:pk>', views.ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense/delete/<int:pk>', views.ExpenseDeleteView.as_view(), name='expense_delete'),
    path('expense/', views.ExpenseList.as_view(), name='expense_list'),  
]