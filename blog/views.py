from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, template_name='blog/index.html')


def posts(request):
    ...


def post_detail(request):
    ...
