from django.contrib.gis.db.models import PointField
from django.db import models

class Peak(models.Model):
  location = PointField()
  altitude = models.IntegerField()
  name = models.CharField(max_length=512)