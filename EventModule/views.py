from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

# Create your views here.


class EventsListView(ListView):
    model = models.Events
    template_name = 'index.html'
    context_object_name = 'events'


def home(request):
    events = models.Events.objects.all()
    projects = models.ProjectPost.objects.all()
    context = {'events': events, 'projects': projects}
    return render(request, 'index.html', context)
