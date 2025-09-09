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
# class ExpenseCreateView(LoginRequiredMixin, CreateView):
#     model = Expense
#     fields = '__all__'
#     success_url = reverse_lazy('expense_list')

from django.forms import ModelForm
from django.views import View
from django.http import HttpResponseRedirect
import datetime

class ArticleForm(ModelForm):
     class Meta:
        model = Expense
        fields = '__all__'
        #exclude = ('user',)

class ExpenseCreateView(View):
    form_class = ArticleForm
    template_name = "templates/finance/costcenter_form.html"
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={"user": request.user, "date": datetime.datetime.now()})
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # new_expense = form.save(commit=False)
            # new_expense.user = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('expense_list'))

        return render(request, self.template_name, {"form": form})


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






   

def detail(request):

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