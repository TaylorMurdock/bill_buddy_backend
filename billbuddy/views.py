from .models import Bills
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BillsSerializer


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [permissions.AllowAny]
