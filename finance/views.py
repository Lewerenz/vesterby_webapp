from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

from django.db.models import Sum

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import CostCenter, Share, Expense
from users.models import CustomUser

import calendar


## CostCenter
# Create
class CostCenterCreateView(LoginRequiredMixin, CreateView):
    model = CostCenter
    fields = '__all__'
    success_url = reverse_lazy('costcenter_list')

# Read
class CostCenterReadView(LoginRequiredMixin, DetailView):
    model = CostCenter

# Update
class CostCenterUpdateView(LoginRequiredMixin, UpdateView):
    model = CostCenter
    fields = '__all__'
    success_url = reverse_lazy('costcenter_list')

# Delete
class CostCenterDeleteView(LoginRequiredMixin, DeleteView):
    model = CostCenter
    success_url = reverse_lazy('costcenter_list')

# List
class CostCenterList(LoginRequiredMixin, ListView):
    model = CostCenter


## Share
# Create
class ShareCreateView(LoginRequiredMixin, CreateView):
    model = Share
    fields = '__all__'
    success_url = reverse_lazy('share_list')

# Read
class ShareReadView(LoginRequiredMixin, DetailView):
    model = Share

# Update
class ShareUpdateView(LoginRequiredMixin, UpdateView):
    model = Share
    fields = '__all__'
    success_url = reverse_lazy('share_list')

# Delete
class ShareDeleteView(LoginRequiredMixin, DeleteView):
    model = Share
    success_url = reverse_lazy('share_list')

# List
class ShareList(LoginRequiredMixin, ListView):
    model = Share

    def get_queryset(self):
        new_context = self.model.objects.filter(user=self.request.user)
        return new_context

## Expense
# Create
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    fields = '__all__'
    success_url = reverse_lazy('expense_list')

# Read
class ExpenseReadView(LoginRequiredMixin, DetailView):
    model = Expense

# Update
class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = '__all__'
    success_url = reverse_lazy('expense_list')

# Delete
class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_list')

# List
class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense

    def get_queryset(self):
        new_context = self.model.objects.filter(user=self.request.user)
        return new_context


# def detail(request):

#     d = CustomUser.objects.get(pk=2).costcenter_set.get(pk=1).payment_set.get(pk=1)
#     # write your view processing logics here
#     return HttpResponse("Welcome to Dashboard" + str(d.amount))

class CustomHTMLCal(calendar.HTMLCalendar):
    cssclasses = [style + " text-red" for style in calendar.HTMLCalendar.cssclasses]
    #cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun red"]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-center text-italic lead"
    cssclass_year_head = "table"




def detail(request):

    kalenderblatt = CustomHTMLCal(calendar.MONDAY)
    ausgabe = kalenderblatt.formatyear(2025,3)

    for day_number in kalenderblatt.iterweekdays():
        print(day_number)

    return render(request, 'finance/calendar.html', {'calendar': ausgabe})    

def my_costs(request):

    kosten_list = []

    user = request.user
    sharings = Share.objects.filter(user=user)

    for share in sharings:

        kosten = {}

        costcenter = share.costcenter
        costs = Expense.objects.filter(costcenter=costcenter).aggregate(Sum('amount', default=0))['amount__sum']
        sharing = Share.objects.filter(costcenter=costcenter).aggregate(Sum('share', default=0))['share__sum']

        fak = costs/sharing

        share = Share.objects.filter(user=user).filter(costcenter = costcenter).aggregate(Sum('share', default=0))['share__sum']
        gesamtkosten = fak * share

        kosten['gesamtkosten'] = gesamtkosten
        kosten['costcenter'] = costcenter

        kosten_list.append(kosten)

    return render(request, 'finance/mycosts.html', {'kosten': kosten_list})