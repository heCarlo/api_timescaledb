from django.db import models

class WeatherEntity(models.Model):
    datetime = models.DateTimeField()
    code = models.CharField(max_length=50)
    direction = models.FloatField(max_length=50)
    temperature = models.FloatField()
    rh = models.FloatField()
    pressure = models.FloatField()
    precip = models.FloatField()
    prmsl = models.FloatField()
    tmpsrf = models.FloatField()
    vel_gfs = models.FloatField()
    vel_twr = models.FloatField()

    def __str__(self):
        return f"Weather Data at {self.datetime}"
