from main.models import Peak
from rest_framework import serializers, viewsets

class PeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peak
        fields = ['location', 'altitude', 'name']

# ViewSets define the view behavior.
class PeakViewSet(viewsets.ModelViewSet):
    queryset = Peaks.objects.all()
    serializer_class = PeakSerializer