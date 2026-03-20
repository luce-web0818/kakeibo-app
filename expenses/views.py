from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from datetime import date

def expense_list(request):
    today = date.today()

    expenses = Expense.objects.all().order_by('-date')

    monthly_expenses = Expense.objects.filter(
        date__year=today.year,
        date__month=today.month
    )

    total_amount = sum(expense.amount for expense in monthly_expenses)
    monthly_count = monthly_expenses.count()

    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total_amount': total_amount,
        'monthly_count': monthly_count,
    })

def home(request):
    return render(request, 'expenses/home.html')

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    total_amount = sum(expense.amount for expense in expenses)
    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total_amount': total_amount,
    })

def expense_create(request):
    if request.method == "POST":
        date = request.POST.get("date")
        category = request.POST.get("category")
        amount = request.POST.get("amount")

        Expense.objects.create(
            date=date,
            category=category,
            amount=amount
        )

        return redirect('expense_list')

    return render(request, 'expenses/expense_form.html')

def expense_delete(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect('expense_list')

def expense_edit(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == "POST":
        expense.date = request.POST.get("date")
        expense.category = request.POST.get("category")
        expense.amount = request.POST.get("amount")
        expense.save()

        return redirect('expense_list')

    return render(request, 'expenses/expense_form.html', {'expense': expense})