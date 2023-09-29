from .models import Bills
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BillsSerializer


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [permissions.AllowAny]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
