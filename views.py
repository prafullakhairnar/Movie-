from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAdminUser()]
        return []

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def rate(self, request, pk=None):
        movie = self.get_object()
        rating_value = request.data.get('rating')

        try:
            rating_value = int(rating_value)
        except (ValueError, TypeError):
            return Response({"error": "Rating must be an integer between 1 and 10."},
                            status=status.HTTP_400_BAD_REQUEST)

        if not (1 <= rating_value <= 10):
            return Response({"error": "Rating must be between 1 and 10."},
                            status=status.HTTP_400_BAD_REQUEST)

        rating, created = Rating.objects.update_or_create(
            movie=movie,
            user=request.user,
            defaults={'rating': rating_value}
        )

        return Response({
            "message": "Rating created" if created else "Rating updated",
            "rating": RatingSerializer(rating).data
        })

class MovieRatingsListView(generics.ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = []

    def get_queryset(self):
        movie_id = self.kwargs['pk']
        return Rating.objects.filter(movie_id=movie_id)
