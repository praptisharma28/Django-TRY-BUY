from django.shortcuts import render, redirect


from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
f
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):    
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



