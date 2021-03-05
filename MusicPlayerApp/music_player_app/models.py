from django.db import models

# Create your models here.

class SongModel(models.Model):
    Name_of_the_Song=models.CharField(max_length=100)
    time_Duration=models.IntegerField()
    Upload_time=models.DateTimeField("Published_data : ")

    object = models.Manager()

    def __str__(self):
        return self.Name_of_the_Song