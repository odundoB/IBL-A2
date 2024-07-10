from django.urls import path
from .views import BankCreateView, BranchCreateView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bank/add/', BankCreateView.as_view(), name='bank_add'),
    path('branch/add/', BranchCreateView.as_view(), name='branch_add'),
]
