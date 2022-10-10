from .views import ExpensesSummaryStats, IncomeSourcesSummaryStats
from django.urls import path

urlpatterns = [
    path(
        'expenses_category_data/', ExpensesSummaryStats.as_view(),
        name='expenses-category-data'),
    path(
        'income_sources_data/', IncomeSourcesSummaryStats.as_view(),
        name='income_sources_data')
]
