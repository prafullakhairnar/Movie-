from rest_framework import serializers
from .models import Movie, Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'rating', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate_rating(self, value):
        if not (1 <= value <= 10):
            raise serializers.ValidationError("Rating must be between 1 and 10.")
        return value

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'created_at', 'average_rating', 'ratings']

    def get_average_rating(self, obj):
        return obj.average_rating()
