from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    context_dict = {'name': 'Karim Altom'}
    return render(request, 'rango/about.html', context = context_dict)

