from .models import *
from rest_framework import serializers

class CafeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Cafe
        fields = ('id', 'title', 'address', 'number', 'signature_menu', 'average_price', 'location', 'image', 'likes_count', 'update_at')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Review
        fields = ('url', 'id', 'cafe', 'date', 'image', 'content', 'likes_count', 'unlikes_count')

class Cafe_LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cafe_Like
        fields = ('id', 'cafe')

class Cafe_UnlikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cafe_Unlike
        fields = ('id', 'cafe')

class Review_LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review_Like
        fields = ('id', 'review')

class Review_UnlikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review_Unlike
        fields = ('id', 'review')

