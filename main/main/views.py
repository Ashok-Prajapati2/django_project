
# Import necessary Django modules and dependencies
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import userForm


# Define a view for the homepage
def homepage(request):
    return render(request, "index.html")

# Define a view for the 'about' page
def about(request):
    if request.method == "GET":
        data = request.GET.get('data')
        return render(request, "about.html", {'data': data})
    return render(request, "about.html")

# Define a view for handling a form
def form(request):
    fn = userForm()  # Create an instance of the userForm class
    data = {'form': fn}  # Initialize data with the form instance
    if request.method == 'POST':
        saved_username = request.POST['email']  # Retrieve 'email' parameter from POST request
        saved_pass = request.POST['password']  # Retrieve 'password' parameter from POST request
        data = {
            'username': saved_username,
            'passwd': saved_pass,
            'form': fn,
        }
        url = "/about/?data={}".format(data)  # Construct a URL with data parameters
        return HttpResponseRedirect(url)  # Redirect to the 'about' page with data parameters
    return render(request, "form.html", data)  # Render the form.html template with data

# Define a view for submitting a form
def submitform(request):
    data = {}
    if request.method == 'POST':
        saved_username = request.POST.get('email')  # Retrieve 'email' parameter from POST request
        saved_pass = request.POST.get('password')  # Retrieve 'password' parameter from POST request
        data = {
            'username': saved_username,
            'passwd': saved_pass,
        }
    return HttpResponse(data['username'])  # Return the 'username' as an HTTP response

# Define a view for a calculator
def calculator(request):
    ans = None  # Initialize ans to None
    if request.method == 'POST':
        try:
            display_value = request.POST.get('display', '')
            ans = eval(display_value)  # Calculate the result using eval
        except Exception as e:
            # Handle any potential errors here, e.g., division by zero
            ans = 'Error'
    return render(request, "calculator.html", {"ans": ans})  # Render the calculator.html template with the result



















