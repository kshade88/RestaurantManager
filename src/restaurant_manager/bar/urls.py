from django.urls import path
from bar import views

urlpatterns = [
    path('spirits/', views.spirit_list, name='spirit-list'),
    path('spirits/<int:pk>/', views.spirit_detail, name='spirit-detail'),
    path('spirits/create/', views.SpiritDetailView.as_view(), name='spirit-create'),
]