from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"signup/pr.html")

def signin2(request):
    return render(request,"signup/signin.html")

def signup(request):
    return render(request,"signup/signup.html")

def handle_login(request):
    if request.method == 'POST': 
        username = request.POST.get ('username') 
        password = request.POST.get ('password')

        return HttpResponse(f"Username: {username} Password: {password} ")
    else:

     return HttpResponse("Invalid request")
    
def handle_logout(request):
    if request.method == 'POST': 
        username = request.POST.get ('username') 
        password = request.POST.get ('password')
        email = request.POST.get ('email')
        mobile = request.POST.get ('mobile')
        return HttpResponse(f"Username: {username} Password: {password} Email: {email} Mobile: {mobile} ")
    else:

     return HttpResponse("Invalid request")
    


