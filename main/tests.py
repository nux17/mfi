from django.test import TestCase
from django.contrib.gis.geos import Point
from main.models import Peak
from rest_framework.test import APIRequestFactory


# Using the standard RequestFactory API to create a form POST request
class PeaksBoundaryTest(TestCase):
    def setUp(self):
        Peak.objects.create(name="Peak1", altitude=0, location=Point(0, 0))
        Peak.objects.create(name="Peak2", altitude=0, location=Point(10, 10))
        Peak.objects.create(name="PeakOut", altitude=0, location=Point(50, 50))

    def test_boundaries(self):
        """
        Checks boundaries filter feature
        """
        factory = APIRequestFactory()
        request = self.client.get('/peaks/?boundaries=[[0.0,0.0],[5.0,5.0],[10.0,10.0],[0.0,0.0]]')
        assert request.data[0]["name"] == "Peak1"
        assert request.data[1]["name"] == "Peak2"
        assert len(request.data) == 2

