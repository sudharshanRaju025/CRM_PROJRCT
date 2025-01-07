from django.urls import path,include
from .views import Courseviewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Course', Courseviewset, basename='course')

urlpatterns = [
    path('', include(router.urls)),  # Include all the routes from the router
]