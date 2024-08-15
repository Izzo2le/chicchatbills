from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('bills/', views.bill_list_view, name='bill_list'),
    path('bills/create/', views.create_bill_view, name='create_bill'),
    path('bills/<int:bill_id>/', views.bill_detail_view, name='bill_detail'),
    path('bills/<int:bill_id>/add-item/', views.add_item_view, name='add_item'),
    path('', views.bill_list, name='bill_list'),
    path('bill/<int:bill_id>/', views.bill_detail, name='bill_detail'),
]
]
