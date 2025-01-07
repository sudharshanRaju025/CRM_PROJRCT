from rest_framework import serializers
from .models import Learner

class Learnerserializers(serializers.ModelSerializer):

    class Meta:

        model=Learner
        fields="__all__"
