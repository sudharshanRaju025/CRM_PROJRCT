from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import opportunityviewset

router = DefaultRouter()

router.register(r"Opportunities",opportunityviewset)
urlpatterns=[
    path("",include(router.urls))
]