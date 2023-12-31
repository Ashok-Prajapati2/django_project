
# Import necessary Django modules and dependencies
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import userForm
from myapp.models import Service
from  news.models import news
from  savedata.models import Savedata
from django.core.paginator import Paginator

# Define a view for the homepage
def homepage(request):
    sdata = Service.objects.all().order_by('title')
    newdata = news.objects.all().order_by('title')[ :4]
    
    
    
    if request.method=='GET': 

        st = request.GET.get('ser')
        if st != None:
            sdata = Service.objects.filter(title__icontains=st)
   
    
    context = {
        'data' : sdata,
        'ndata': newdata,
       
    }
    return render(request, "index.html" , context )

def service(request):
    
    sdata = Service.objects.all().order_by('title')
    paginator = Paginator(sdata,2)
    page_num = request.GET.get('page')
    sdataf = paginator.get_page(page_num)
    
    if request.method=='GET':
        st = request.GET.get('ser')
        if st != None:
            sdata = Service.objects.filter(title__icontains=st)
   
    context = {
        'data' : sdata,
        'sdata' : sdataf,
        'page_num ':page_num 
    }
    return render(request, "service.html" , context )

# Define a view for the 'about' page
def savedata(request):
   
    if request.method == 'POST':
        saved_username = request.POST.get('email')  # Retrieve 'email' parameter from POST request
        saved_pass = request.POST.get('password')   # Retrieve 'password' parameter from POST request
        if saved_username and saved_pass != '':
            Savedata.objects.create(usertitle=saved_username, userdest=saved_pass)
    return render(request, "savedata.html" )
 
def newsd(request,id):
    
    newdata = news.objects.get(news_slug = id)
    data = {
         'newst': newdata
        
    }
    return render(request, "news.html",data)

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

def calculator(request):
    ans = None  # Initialize ans to None
    list = ['ashok', 'ramesh', 'rahul']  # Renamed variable to 'my_list'
    my_dict = [
        {
        'name': "ASHOK",
        'm': 8696,  },
        {
        'name': "ASHOK",    
        'm': 9312, 
        }
        ]
    if request.method == 'POST':
        try:
            display_value = request.POST.get('display', '')
            ans = eval(display_value)  # Calculate the result using eval
        except Exception as e:
            ans = 'Error'

    return render(request, "calculator.html", {"ans": ans, "list": list, 'dict': my_dict})



def coid(request, id):
    return HttpResponse(id)
















