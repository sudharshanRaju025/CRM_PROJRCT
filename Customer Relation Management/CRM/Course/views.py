from django.shortcuts import render
from rest_framework import viewsets
from .serializers import courseserializers
from .models import Course

# Create your views here.

class Courseviewset(viewsets.ModelViewSet):
      
    queryset=Course.objects.all()
    serializer_class=courseserializers
    
    