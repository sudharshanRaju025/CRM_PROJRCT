from rest_framework import serializers
from .models import leads
import re
from django.utils import timezone

class Leadserializers(serializers.ModelSerializer):

    class Meta :

        model= leads
        fields="__all__"

    def clean_Email(self):
        email=self.cleaned_data.get("Email")
        pattern=r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern,email):
            raise serializers.ValidationError("Email field is required")
        return email

    def get_start_time(self, obj):
        naive_time = timezone.make_naive(obj.start_time)
        return naive_time.strftime('%Y-%m-%d %H:%M:%S')