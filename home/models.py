from django.db import models


class File(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='pics')
    Description = models.TextField()
    Season = models.IntegerField()
    Episode = models.IntegerField()

