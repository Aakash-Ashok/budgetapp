from rest_framework import serializers
from api.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Transaction
        fields="__all__"
        read_only_fields=["id","created_date"]