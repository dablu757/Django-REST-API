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
    category = CategorySerializer()  # Serialize the related Category model

    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category')  # Extract category data
        category, created = Category.objects.get_or_create(**category_data)  # Get or create the Category instance
        book = Books.objects.create(category=category, **validated_data)  # Create the Book instance
        return book

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')  # Extract category data
        category, created = Category.objects.get_or_create(**category_data)  # Get or create the Category instance
        instance.category = category
        instance.book_tiltle = validated_data.get('book_tiltle', instance.book_tiltle)
        instance.save()  # Update the Book instance
        return instance


# class BookSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     class Meta:
#         model = Books
#         fields = '__all__'

#     def create(self, validated_data):
#         # Extract the nested category data
#         category_data = validated_data.pop('category')
#         # Get or create the category instance
#         category, created = Category.objects.get_or_create(**category_data)
#         # Create the book instance with the category instance
#         book = Books.objects.create(category=category, **validated_data)
#         return book

#     def update(self, instance, validated_data):
#         # Extract the nested category data
#         category_data = validated_data.pop('category')
#         # Get or create the category instance
#         category, created = Category.objects.get_or_create(**category_data)
        
#         # Update the book instance with the new category and other validated data
#         instance.category = category
#         instance.book_title = validated_data.get('book_title', instance.book_title)
#         instance.save()
#         return instance


