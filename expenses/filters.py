import django_filters
from rest_framework.exceptions import ValidationError

from expenses.models import Expense


class ExpenseFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Expense
        fields = ['user', 'start_date', 'end_date']


class ExpenseSummaryFilter(django_filters.FilterSet):
    month = django_filters.NumberFilter(method="filter_month", field_name="date", lookup_expr="month")

    class Meta:
        model = Expense
        fields = ['user', 'month']

    def filter_month(self, queryset, name, value):
        if not (1 <= value <= 12):
            raise ValidationError("Month must be between 1 and 12.")
        return queryset.filter(**{f"{name}__month": value})
