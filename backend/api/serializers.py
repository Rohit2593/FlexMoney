from rest_framework import serializers
from .models import User, Payment

class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    user_email = serializers.CharField()
    user_age = serializers.IntegerField()
    user_batch = serializers.IntegerField()
    payment_details = serializers.CharField()
