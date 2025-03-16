from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

from django.db.models import Sum

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import CostCenter, Sharing, Expense
from users.models import CustomUser


class CostcenterDetailView(DetailView):
    model = CostCenter

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
        new_context = Expense.objects.filter(user=self.request.user)
        return new_context




# def detail(request):

#     d = CustomUser.objects.get(pk=2).costcenter_set.get(pk=1).payment_set.get(pk=1)
#     # write your view processing logics here
#     return HttpResponse("Welcome to Dashboard" + str(d.amount))

def detail(request):

    print(request.user)

    user = request.user
    costcenter = CostCenter.objects.get(pk=3)

    share = Sharing.objects.filter(user=user).filter(costcenter = costcenter).aggregate(Sum('share', default=0))['share__sum']
    costs = Expense.objects.filter(costcenter=costcenter).aggregate(Sum('amount', default=0))['amount__sum']
    payments = Expense.objects.filter(user=user).filter(costcenter=costcenter).aggregate(Sum('amount', default=0))['amount__sum']
    sharing = Sharing.objects.filter(costcenter=costcenter).aggregate(Sum('share', default=0))['share__sum']

    fak = costs/sharing
    gesamtkosten = fak * share
    minuseigen = gesamtkosten -payments

    string = ' | User: ' + user.username + ' | share: ' + str(share) + ' | CostCenter: ' + costcenter.name + ' | costs: ' + str(costs) + ' | sharing: ' +  str(sharing) + ' | fak: ' +  str(fak) + ' | gesamtkosten: ' +  str(gesamtkosten) + ' | minuseigen: ' +  str(minuseigen)

    # write your view processing logics here
    # return HttpResponse(
    #                     )

    return render(request, 'finance/personalcostcenter.html', {'string': string})            

def my_costs(request):

    kosten_list = []

    user = request.user
    sharings = Sharing.objects.filter(user=user)

    for share in sharings:

        kosten = {}

        costcenter = share.costcenter
        costs = Expense.objects.filter(costcenter=costcenter).aggregate(Sum('amount', default=0))['amount__sum']
        sharing = Sharing.objects.filter(costcenter=costcenter).aggregate(Sum('share', default=0))['share__sum']

        fak = costs/sharing

        share = Sharing.objects.filter(user=user).filter(costcenter = costcenter).aggregate(Sum('share', default=0))['share__sum']
        gesamtkosten = fak * share

        kosten['gesamtkosten'] = gesamtkosten
        kosten['costcenter'] = costcenter

        kosten_list.append(kosten)

    return render(request, 'finance/mycosts.html', {'kosten': kosten_list})