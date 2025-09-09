from django.shortcuts import render

from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event, Visit

import calendar
from datetime import date


## Event
# Create
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('event_list')

# Read
class EventReadView(LoginRequiredMixin, DetailView):
    model = Event

# Update
class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('event_list')

# Delete
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')

# List
class EventList(LoginRequiredMixin, ListView):
    model = Event


## Visit
# Create
class VisitCreateView(LoginRequiredMixin, CreateView):
    model = Visit
    fields = '__all__'
    success_url = reverse_lazy('visit_list')
    def get_form(self):
        form = super().get_form()
        form.fields['startdate'].widget = DatePickerInput()
        form.fields['enddate'].widget = DatePickerInput()
        return form


# Read
class VisitReadView(LoginRequiredMixin, DetailView):
    model = Visit

# Update
class VisitUpdateView(LoginRequiredMixin, UpdateView):
    model = Visit
    fields = '__all__'
    success_url = reverse_lazy('visit_list')
    def get_form(self):
        form = super().get_form()
        form.fields['startdate'].widget = DatePickerInput()
        form.fields['enddate'].widget = DatePickerInput()
        return form

# Delete
class VisitDeleteView(LoginRequiredMixin, DeleteView):
    model = Visit
    success_url = reverse_lazy('visit_list')

# List
class VisitList(LoginRequiredMixin, ListView):
    model = Visit



class CustomHTMLCal(calendar.HTMLCalendar):
    cssclasses = [style + " text-red" for style in calendar.HTMLCalendar.cssclasses]
    #cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun red"]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-center text-italic lead"
    cssclass_year_head = "table"


def detail(request):

    Kalender = calendar.Calendar(firstweekday=0)
    

    for jahr in Kalender.yeardatescalendar(2025, width=1):
        for month in jahr:
            for week in month:
                for day in week:
                    print(day)
    
    cal = calendar.HTMLCalendar()
    ausgabe = cal.formatyear(2025,1)

    return render(request, 'schedule/calendar.html', {'calendar': ausgabe}) 