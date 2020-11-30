"""
Route definition for peaks objects
"""


import json

from django.contrib.gis.geos import Point
from rest_framework import serializers, viewsets
from drf_extra_fields.geo_fields import PointField
from django.contrib.gis.geos import Polygon

from main.models import Peak


class PeakSerializer(serializers.HyperlinkedModelSerializer):
    location = PointField()

    class Meta:
        model = Peak
        fields = ('id', 'location', 'altitude', 'name')


class PeakViewSet(viewsets.ModelViewSet):
    """
    Provides list view with **GET, POST** methods and detail view with **GET, PUT, PATCH, DELETE** methods.

    Parameters:

    *location*: JSON field containing **longitude** (float) and **latitude** (float) values

    *altitude*: integer

    *name*: string

    Query parameters:

    *boundaries*: JSON list of two points list defining a box, returns all points contained within that box
    eg. [[0.0,0.0],[5.0,5.0],[10.0,10.0],[0.0,0.0]]
    """
    serializer_class = PeakSerializer

    def get_queryset(self):
        queryset = Peak.objects.all()
        boundaries = self.request.query_params.get('boundaries', None)
        try:
            if boundaries is not None:
                boundaries = json.loads(boundaries)
                boundaries = tuple((i[0], i[1]) for i in boundaries)
                poly = Polygon(boundaries)
                queryset = queryset.filter(location__contained=poly)
            return queryset
        except:
            return None