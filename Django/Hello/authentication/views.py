from django.shortcuts import render, redirect

# authentication/views.py
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from authentication.models import Login, Signup
# def login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Change 'home' to your desired URL
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Change 'home' to your desired URL
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'signup.html', {'form': form})

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



