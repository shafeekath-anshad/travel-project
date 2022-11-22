from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class meet_the_team(models.Model):
    img = models.ImageField(upload_to='meet_pic')
    name = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name
