from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet

Router=DefaultRouter()

Router.register(r"leads",LeadViewSet)
urlpatterns=[
    path("",include(Router.urls))
]