from django.contrib.gis.db.models import PointField
from django.contrib.gis.db.models import  Manager as GeoManager
from django.db import models

class Peak(models.Model):
  """
  Peak model defintion, longitude and latitude are contained within the location field
  """
  location = PointField()
  altitude = models.IntegerField()
  name = models.CharField(max_length=512)