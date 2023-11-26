from django.db import models

# Create your models here.


class Events(models.Model):
    eventTitle = models.CharField(max_length=100000)
    eventAddress = models.CharField(max_length=100000)
    eventDescription = models.TextField()
    eventDuration = models.TimeField()
    eventLocation = models.CharField(max_length=100000)
    eventDate = models.DateField()
    eventImage = models.FileField(
        upload_to='Images/events/', max_length=250, null=True, default=None)

    def __str__(self):
        return self.eventTitle


class ProjectPost(models.Model):
    projectDetails = models.CharField(max_length=10000)
    projectMemebers = models.IntegerField()
    projectRating = models.SmallIntegerField()
    projectImage = models.FileField(
        upload_to='Images/project/', max_length=250, null=True, default=True)

    def __str__(self):
        return self.projectDetails



