from django.db import models


class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    duration = models.PositiveIntegerField()
    sensei = models.TextField()

    class Meta:
        app_label = 'huyna'
