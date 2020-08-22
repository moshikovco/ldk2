from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from . import views
# from .views import APIapeals

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

app_name = 'api'
urlpatterns = [
      path('', include(router.urls)),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
      path('form/<str:uid>', views.formpage, name='formpage'),
      path('form/<str:uid>/insert', views.form_insert, name='form_insert'),
      
      path('apeals/', views.APIapeals),
]