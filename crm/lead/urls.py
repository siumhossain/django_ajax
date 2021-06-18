from django.urls import path
from .import views



app_name = 'lead'
urlpatterns = [
    path('', views.homepage,name='home'),
    path('lead/', views.LeadListView.as_view(),name='lead'),
    path('<int:pk>/', views.LeadDetailView.as_view(),name='lead_details'),
    path('<int:pk>/update/', views.LeadUpdateView.as_view(),name='lead_update'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(),name='lead_delete'),
    path('create/', views.LeadCreateView.as_view(),name='lead_create'),
    path('no/', views.No.as_view(),name='no'),


    path('lead/search/', views.search_results,name='search_results'),
    path('sync/', views.lead,name='sync'),
    path('async/', views.lead_async,name='async'),
    

    
]