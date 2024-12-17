from django.urls import path
from . import views

urlpatterns=[
    path('',views.medicine_list,name='medicine_list'),
    path('delete/<int:id>/', views.delete_medicine, name='delete'),
]