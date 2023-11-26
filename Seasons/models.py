from django.db import models

# Create your models here.


class Season(models.Model):
    seasonName = models.CharField(max_length=10000)
    seasonSpeaker = models.CharField(max_length=1000, null=True)
    seasonDescription = models.CharField(max_length=1000)
    seasonDuration = models.CharField(max_length=2)
    seasonDate = models.DateField(null=True)
    seasonLocation = models.CharField(max_length=1000, null=True)
    seasonImage = models.FileField(
        upload_to='Images/Seasons/', max_length=250, null=True, default=None)
    seasonContactPhoneNumber_1 = models.CharField(max_length=10, null=True)
    seasonContactPhoneNumber_2 = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.seasonName
