from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from authentication.models import Login,Signup


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
    if request.method=="POST":
        print(request)
        Username = request.POST['Username']
        Password = request.POST['Password']
        print(Username, Password)
        login=Login(Username=Username,Password=Password)
        login.save()
    return render(request,'login.html')
def signup(request):
    if request.method=="POST":
        print(request)
        Username = request.POST['Username']
        Password = request.POST['Password']
        Confirm_Password = request.POST['Confirm_Password']
        print(Username, Password)
        signup=Signup(Username=Username,Password=Password,Confirm_Password=Confirm_Password)
        signup.save()
    return render(request,'signup.html')

