from django.db import models

# Create your models here.


class Events(models.Model):
    eventTitle = models.CharField(max_length=100000)
    eventAddress = models.CharField(max_length=100000)
    eventDescription = models.TextField()
    eventDuration = models.TimeField()
    eventLocation = models.CharField(max_length=100000)
    eventDate = models.DateField()

    def __str__(self):
        return self.eventTitle


class ProjectPost(models.Model):
    projectDetails = models.CharField(max_length=10000)
    projectMemebers = models.IntegerField()
    projectRating = models.SmallIntegerField()

    def __str__(self):
        return self.projectDetails
