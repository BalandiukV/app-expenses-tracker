from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExpenseListCreateView.as_view(), name="expense-list-create"),
    path("<int:pk>/", views.ExpenseDetailView.as_view(), name="expense-detail"),
    path("<int:user_id>/date-range/", views.ExpenseByDateRangeView.as_view(), name="expense-date-range"),
    path("<int:user_id>/category-summary/<int:month>/", views.CategorySummaryView.as_view(), name="category-summary"),
]
