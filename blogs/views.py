from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from blogs.forms import formBlogs
from blogs.models import myBlogs
from django.core.paginator import Paginator

from django.contrib.auth import login,logout,authenticate

# Create your views here.
def homepage(request):
	mydata = myBlogs.objects.all().filter(active=True).order_by("-id")
	newdata = mydata[0]
	olddata = mydata[1:]
	p=Paginator(olddata,3)
	pagenya = request.GET.get('p')
	
	if pagenya==None:
		pagenya=1
	else:
		if isinstance(pagenya,str):
			pagenya=1
	try:
		lihatlah = p.get_page(pagenya)
	except:
		lihatlah = p.get_page(1)

	return render(request,'blogs/dashboard.html',{'olddata':lihatlah,'newdata':newdata})

def admin_page(request):
	username=None
	password=None
	try:
		if request.method=="POST":
			username = request.POST['txtUsername']
			password = request.POST['txtPassword']
	except:
		pass

	if username!=None:
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
		return HttpResponseRedirect('/blogs/adm/')
		print(username)
	else:
		if request.method == "POST":
			forms = formBlogs(request.POST, request.FILES)
			if forms.is_valid():
				forms.save()
			else:
				print(forms)
		forms = formBlogs()
		return render(request,'blogs/input_admin.html',{'forms':forms})

def logoutme(request):
	logout(request)
	return HttpResponseRedirect('/blogs/adm/')