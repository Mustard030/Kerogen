from rest_framework import viewsets

from api.models import KerogenModel
from api.serializers import KerogenModelSerializer


class KerogenModelViewSet(viewsets.ModelViewSet):
    queryset = KerogenModel.objects.all()
    serializer_class = KerogenModelSerializer
