from django.shortcuts import render

# Create your views here.


def thankyouPage(request):
    return render(request, 'thankyou.html')
