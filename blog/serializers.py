from rest_framework import serializers

from .models import BlogModel, Categories


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Categories
        fields = ['category_id', 'category_name']

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = BlogModel
        fields = [
            'id', 'title', 'content', 'time_to_read', 
            'categories', 'image', 'date_posted'
        ]

    def create(self, validated_data):
        category_data = validated_data.pop('categories')
        blog, created = BlogModel.objects.get_or_create(**validated_data)

        cat_list= []
        for category in category_data:
            cat, created = Categories.objects.get_or_create(**category)
            cat_list.append(cat)

        blog.categories.add(*cat_list)
        return blog 
