from django.db import models


class Exercises(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    distance = models.FloatField(db_index=True)
    moving_time = models.IntegerField(db_index=True)
    total_elevation_gain = models.IntegerField(db_index=True)
    time_stamp = models.DateTimeField(db_index=True, null=True)

    class Meta:
        db_table = 'exercises'

# Create your models here.
