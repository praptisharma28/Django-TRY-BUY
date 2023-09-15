from django.shortcuts import render
from django.http import HttpResponse

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
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')
        print(name, email, message)
    return render(request,'contact.html')
