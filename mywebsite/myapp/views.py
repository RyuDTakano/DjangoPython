from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Homepage(requst):
    return HttpResponse("<h2>gundam</h2>")

