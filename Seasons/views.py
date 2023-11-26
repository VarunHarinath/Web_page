from django.shortcuts import render
from .models import Season

# Create your views here.


def seasons(request):
    season = Season.objects.all()
    context = {'seasons': season}
    return render(request, 'meeting-details.html', context=context)
