from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect


def homepage(request):
    
    return render(request, "index.html")


def about(request):
    
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
            # return HttpResponseRedirect("/about/")
    
        return render(request, "form.html", data)


