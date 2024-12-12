from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ['id', 'user', 'title', 'amount', 'date', 'category']


class ExpenseSummarySerializer(serializers.Serializer):
    category = serializers.CharField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)

    class Meta:
        fields = ['total', 'category']
