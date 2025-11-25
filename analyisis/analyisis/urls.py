from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from climate_api import views

# Создание маршрутов для ViewSet
router = DefaultRouter()
router.register(r'climate-data', views.ClimateDataViewSet, basename='climate-data')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Индивидуальные endpoints
    path('api/city-statistics/', views.CityStatisticsView.as_view(), name='city-statistics'),
    path('api/compare-cities/', views.CompareCitiesView.as_view(), name='compare-cities'),
    path('api/extreme-days/', views.FindExtremeDaysView.as_view(), name='extreme-days'),
    path('api/upload-data/', views.UploadClimateDataView.as_view(), name='upload-climate-data'),
    
    # ViewSet endpoints
    path('api/', include(router.urls)),
]