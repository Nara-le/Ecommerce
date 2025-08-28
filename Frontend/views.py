from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'title':'home'})
def index(request):
    return render(request,'index.html',{'title':'index'})