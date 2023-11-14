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
    context = {'events': events, 'projects': projects}
    return render(request, 'index.html', context)
