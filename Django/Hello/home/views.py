from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
# Create your views here.
# def index(request):
#     return HttpResponse("This is homepage")

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name, email, message)
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
