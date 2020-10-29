from rest_framework import serializers
from moviesapp.models import Movies


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ('name','popularity','director','imdb_score')