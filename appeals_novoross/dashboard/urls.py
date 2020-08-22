from django.urls import path, include

from . import views

app_name = 'dashboard'
urlpatterns = [

    path('', views.index, name='dashboard'),
    path('apeals', views.apeals, name='apeals'),
    path('apeals/details/<int:apeals_id>', views.apeals_details, name='apeals_details'),
    
]