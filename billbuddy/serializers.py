from .models import Bills
from rest_framework import serializers


class BillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bills
        fields = ['id', 'name_of_subscription',
                  'subscription_image_url', 'bill_date', 'subscription_price']
