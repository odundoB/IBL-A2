from django.urls import path
from .views import HomeView, BankCreateView, BranchCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='dashboard'),  # Dashboard/home view
    path('bank/add/', BankCreateView.as_view(), name='bank_add'),
    path('branch/add/', BranchCreateView.as_view(), name='branch_add'),
]
