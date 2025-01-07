from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Learnerviews

Router=DefaultRouter()

Router.register(r"Learner",Learnerviews)

urlpatterns=[
    path("",include(Router.urls)),
]