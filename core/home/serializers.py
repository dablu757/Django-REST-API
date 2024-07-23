from rest_framework import serializers
from .models import UserDetails

class UserDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserDetails
        # fields = ['name', 'email']  # For serializer, only selected fields
        # exclude = ['id'] # For serializer to exclude some fields
        fields = '__all__' # For serializer to include all fields
