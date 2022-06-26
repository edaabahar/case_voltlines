from django.db.models import fields
from rest_framework import serializers
from .models import Passenger, PassengerTrips

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
class PassengerTripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerTrips
        fields = '__all__'