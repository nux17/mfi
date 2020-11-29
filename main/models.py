from django.contrib.gis.db.models import PointField
from django.contrib.gis.db.models import  Manager as GeoManager
from django.db import models

class Peak(models.Model):
  location = PointField()
  altitude = models.IntegerField()
  name = models.CharField(max_length=512)