from rest_framework import serializers
from .models import *
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        # fields = ['name', 'email']  # For serializer, only selected fields
        # exclude = ['id'] # For serializer to exclude some fields
        fields = '__all__' # For serializer to include all fields

        def validate(self, data):
            #name should be in alphabet only
            if data['name']:
                for name in data['name']:
                    if name.isdigit():
                        raise serializers.ValidationError(
                            {
                                'Error' : 'name should be in alphabet only'
                            }
                        )
            #email should contain @ character
            if data['email']:
                for c in data['email']:
                    if '@' not in c:
                        raise serializers.ValidationError({
                            'error' : "please enter valid email id"
                        })
                    
            # mobile number len should be 10 and not contain any alphabet
            if data['phone_no']:
                if len(data['phone_no']<10):
                    raise serializers.ValidationError({'error' : 'please enter 10 digit valid mobile number'})
                for number in data['phone_no']:
                    if number.isalpha():
                        raise serializers.ValidationError({'error': 'pleae enter 10 digit integer mobile no'})
            
            return data
        



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


