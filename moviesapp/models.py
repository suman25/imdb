from djongo import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length= 100)
    popularity = models.FloatField()
    director = models.CharField(max_length=100)
    imdb_score = models.FloatField()

