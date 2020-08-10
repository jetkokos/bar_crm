from django.urls import path
from main import views

urlpatterns = [
    path('', views.dashboardView, name='dashboard'),
    path('expenses/', views.expensesView, name='expenses'),
    path('proceed/', views.proceedView, name='proceed'),
    path('reports/', views.reportsView, name='reports'),
    path('create_report/', views.createReportView, name='create_report'),
    path('update_report/', views.updateReportView, name='update_report'),
    
]

