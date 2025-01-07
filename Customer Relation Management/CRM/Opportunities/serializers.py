from rest_framework import serializers
from .models import Opportunities

class Opportunityserializers(serializers.ModelSerializer):

    class Meta:
         model=Opportunities
         fields="__all__"