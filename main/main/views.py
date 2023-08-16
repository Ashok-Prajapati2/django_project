from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    
    return render(request, "index.html")


def form(request):
    
    return render(request,"form.html")


def about(request):
    
    return render(request, "about.html")

def user_login(request):
        if request.method == 'GET'
            saved_username = request.GET.get('email')  # Retrieve the 'email' parameter from the GET request
            saved_pass = request.GET.get('text')   # Retrieve the 'text' parameter from the GET request
        

        return render(request, "form.html", {'username': saved_username , 'passwd':saved_pass})
