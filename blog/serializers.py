from rest_framework import serializers

from .models import BlogModel, Categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = BlogModel
        fields = [
            'id', 'title', 'content', 'time_to_read', 
            'categories', 'image', 'date_posted'
        ]
