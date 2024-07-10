from django.shortcuts import render, redirect
from django.views import View
from .models import Bank, Branch
from .forms import BankForm, BranchForm

class HomeView(View):
    def get(self, request):
        return render(request, 'banks/home.html')

class BankCreateView(View):
    def get(self, request):
        form = BankForm()
        return render(request, 'banks/bank_form.html', {'form': form})

    def post(self, request):
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank_add')
        return render(request, 'banks/bank_form.html', {'form': form})

class BranchCreateView(View):
    def get(self, request):
        form = BranchForm()
        return render(request, 'banks/branch_form.html', {'form': form})

    def post(self, request):
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_add')
        return render(request, 'banks/branch_form.html', {'form': form})
