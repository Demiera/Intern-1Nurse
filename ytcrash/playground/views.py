from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def caculate():
    x=1
    y=2
    z = x + y
    return z

def starter(request):

    return render(request, 'playground/index.html', {'name':'Dodo'})