from django.shortcuts import render
from django.views.generic.detail import DetailView
from . import models
from ContactForm.models import ContactForm
# Create your views here.


class Detailview(DetailView):
    model = models.Events
    template_name = 'meeting-details.html'
    context_object_name = 'detail'


def home(request):
    events = models.Events.objects.all()
    projects = models.ProjectPost.objects.all()
    context = {'events': events, 'projects': projects}

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        UserForm = ContactForm(name=name, email=email, message=message)
        UserForm.save()
        print("hi")

    return render(request, 'index.html', context)
