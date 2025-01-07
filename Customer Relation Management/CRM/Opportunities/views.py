from django.shortcuts import render
from rest_framework import viewsets
from .models import Opportunities
from .serializers import Opportunityserializers

# Create your views here.

class opportunityviewset(viewsets.ModelViewSet):

    queryset=Opportunities.objects.all()
    serializer_class=Opportunityserializers

