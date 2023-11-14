from django.shortcuts import render
from django.views.generic.detail import DetailView
from . import models

# Create your views here.


class Detailview(DetailView):
    model = models.Events
    template_name = 'meeting-details.html'
    context_object_name = 'detail'


def home(request):
    events = models.Events.objects.all()
    projects = models.ProjectPost.objects.all()
    MONTH = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SPT','OCT','NOV','DEC']
    date = models.Events.eventDate.date()
    context = {'events': events, 'projects': projects,'date':date}
    return render(request, 'index.html', context)
