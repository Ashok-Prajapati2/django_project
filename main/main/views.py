from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render ,redirect
import json


def homepage(request):
    
    return render(request, "index.html")

def about(request):
    if request.method == "GET":
        data = request.GET.get('data')
       
        return render(request, "about.html",{'data':data})

    return render(request, "about.html")

def form(request):
        data = {}
        if request.method == 'POST':
            saved_username = request.POST['email']  # Retrieve the 'email' parameter from the GET request
            saved_pass = request.POST['password']  # Retrieve the 'text' parameter from the GET request
            data = { 
                'username': saved_username,
                'passwd':saved_pass,
                }
            url = "/about/?data={}".format(data)
            return HttpResponseRedirect(url)
    
        return render(request, "form.html", data)



def submitform(request):
        data = {}
        if request.method == 'POST':
            saved_username = request.POST.get('email') # Retrieve the 'email' parameter from the GET request
            saved_pass = request.POST.get('password') # Retrieve the 'text' parameter from the GET request
            data = { 
                'username': saved_username,
                'passwd':saved_pass,
                }
        return HttpResponse(data['username'])





































