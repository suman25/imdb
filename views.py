from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from moviesapp.models import Movies
from moviesapp.serializers import MovieSerializer


# Create your views here.
class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()
    pagination_class = PageNumberPagination
    filter_backends =(OrderingFilter,SearchFilter)
    ordering_fields = ('popularity', 'imdb_score')
    search_fields = ('name','director', 'imdb_score', 'popularity')
