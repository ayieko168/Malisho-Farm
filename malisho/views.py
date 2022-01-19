from django.shortcuts import render, HttpResponse, redirect

def homeView(request):
    
    return render(request, 'index.html')