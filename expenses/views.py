from datetime import datetime

from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Sum
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseByDateRangeView(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        date_default = datetime.utcnow().date()

        start_date = self.request.query_params.get('start_date', date_default)
        end_date = self.request.query_params.get('end_date', date_default)
        return Expense.objects.filter(
            user_id=user_id,
            date__range=[start_date, end_date]
        )


class CategorySummaryView(generics.ListAPIView):
    def get(self, request, user_id, month):
        expenses = Expense.objects.filter(
            user_id=user_id,
            date__month=month
        ).values('category').annotate(total=Sum('amount'))

        return Response(expenses, status=status.HTTP_200_OK)
