from django.urls import path

from . import views 

urlpatterns = [
    path('', views.my_costs, name="detail"),

    path('costcenter/create', views.CostCenterCreateView.as_view(), name='costcenter_create'),
    path('costcenter/read/<int:pk>', views.CostCenterReadView.as_view(), name='costcenter_read'),
    path('costcenter/update/<int:pk>', views.CostCenterUpdateView.as_view(), name='costcenter_update'),
    path('costcenter/delete/<int:pk>', views.CostCenterDeleteView.as_view(), name='costcenter_delete'),
    path('costcenter/', views.CostCenterList.as_view(), name='costcenter_list'), 

    path('share/create', views.ShareCreateView.as_view(), name='share_create'),
    path('share/read/<int:pk>', views.ShareReadView.as_view(), name='share_read'),
    path('share/update/<int:pk>', views.ShareUpdateView.as_view(), name='share_update'),
    path('share/delete/<int:pk>', views.ShareDeleteView.as_view(), name='share_delete'),
    path('share/', views.ShareList.as_view(), name='share_list'),

    path('expense/create', views.ExpenseCreateView.as_view(), name='expense_create'),
    path('expense/read/<int:pk>', views.ExpenseReadView.as_view(), name='expense_read'),
    path('expense/update/<int:pk>', views.ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense/delete/<int:pk>', views.ExpenseDeleteView.as_view(), name='expense_delete'),
    path('expense/', views.ExpenseList.as_view(), name='expense_list'), 
]