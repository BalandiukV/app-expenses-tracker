from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, filters
from rest_framework.response import Response
from django.db.models import Sum

from .filters import ExpenseFilter, ExpenseSummaryFilter
from .models import Expense
from .serializers import ExpenseSerializer, ExpenseSummarySerializer


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ExpenseFilter


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CategorySummaryView(generics.ListAPIView):
    serializer_class = ExpenseSummarySerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ExpenseSummaryFilter

    def get_queryset(self):
        return Expense.objects.values('category').annotate(
            total=Sum('amount')
        )
