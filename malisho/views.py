from curses.ascii import HT
from django.shortcuts import render, HttpResponse, redirect

def homeView(request):
    
    return render(request, 'index.html')