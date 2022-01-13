from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  index(request):
    return render(request, 'quote_generator/index.html')

# def  index(request):
#     return render(request, 'exchange_rate/index.html')

# def  about(request):
#     return render(request, 'quote_generator/about.html')