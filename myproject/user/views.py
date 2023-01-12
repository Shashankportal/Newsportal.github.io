from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
	cdata=category.objects.all().order_by('-id')[0:6]
	ndata=news.objects.all().order_by('-id')[0:6]
	data=notification.objects.all().order_by('-id')[0:4]
	sdata=slider.objects.all().order_by('-id')
	return render(request,'user/index.html',{"data":cdata,"news":ndata,"notification":data,"slider":sdata})

def about(request):
	return render(request,'user/about.html')

def videogallery(request):
	vdata=video.objects.all().order_by('-id')
	return render(request,'user/videos.html',{'video':vdata})

def contactus(request):
	status=False
	if request.method=='POST':
		Name=request.POST.get("name","")
		Email=request.POST.get("email","")
		Mobile=request.POST.get("mobile","")
		Message=request.POST.get("msg","")
		x=contact(name=Name,email=Email,mobile=Mobile,message=Message)
		x.save()
		status=True
	return render(request,'user/contactus.html',{'S':status})

def viewmore(request):
	a = request.GET.get('msg')
	ndata = news.objects.filter(id=a)
	return render(request, 'user/viewmore.html', {"data": ndata})

def vnews(request):
	cdata=category.objects.all().order_by('-id')

	a=request.GET.get('abc')
	ndata=""
	if a is None:
		ndata=news.objects.all().order_by('-id')
	else:
		ndata=news.objects.filter(ncategory=a)
	return render(request,'user/viewnews.html',{"c": cdata,"n":ndata})


def services(request):
	return render(request,'user/services.html')
		
def login(request):
	return render(request,'user/login.html')
def signup(request):
	if request.method=='Post':
		name=request.Post.get("name","")
		email=request.Post.get("email","")
		mobile=request.Post.get("mobile","")
		password=request.Post.get("passwd","")
		address=request.Post.get("address","")
		picname=request.FILES['fu']
		profile(name=name,mobile=mobile,email=email,passwd=password,address=address,ppic=picname).save()
	return render(request,'user/signup.html')
