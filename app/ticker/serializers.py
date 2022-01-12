from rest_framework import serializers
from .models import Tick

class TickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tick
        fields = ('epoch_timestamp', 'symbol', 'value')