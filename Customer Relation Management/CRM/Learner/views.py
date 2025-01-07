from django.shortcuts import render
from rest_framework import viewsets
from .models import Learner
from .serializers import Learnerserializers

# Create your views here.

class Learnerviews(viewsets.ModelViewSet):

    queryset=Learner.objects.all()
    serializer_class=Learnerserializers