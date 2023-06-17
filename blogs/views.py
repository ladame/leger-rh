from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from blogs.forms import formBlogs
from blogs.models import myBlogs
from django.core.paginator import Paginator

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
	mydata = myBlogs.objects.all().filter(active=True).order_by("-id")
	try:
		newdata = mydata[0]
	except:
		newdata = None
	olddata = mydata[1:]
	p=Paginator(olddata,3)
	try:
		pagenya = int(request.GET.get('p'))
	except:
		pagenya = 1

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

@login_required
def admin_list(request,page):
	if request.method=="POST":
		pass1= request.POST['txtNewPassword1']
		pass2= request.POST['txtNewPassword2']
		if(pass1==pass2):
			username = request.user.username
			password = request.POST['txtOldPassword']
			user = authenticate(username=username,password=password)

			if user != None:
				print('password awal benar')
				usernya = User.objects.get(username=username)
				usernya.set_password(pass1)
				usernya.save()

			else:
				print("password lama salah")
		else:
			print("pass beda")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	mydata = myBlogs.objects.all()

	try:
		halaman=int(page)
	except:
		halaman=1

	p = Paginator(mydata,10)

	if isinstance(page,int):
		if page<1:
			halaman=1
		if page>p.num_pages:
			halaman=1
	else:
		halaman=1

	tampilkanlah = p.get_page(halaman)
	return render(request,'blogs/list_blog.html',{'mydata':tampilkanlah})

@login_required
def update_active(request,pk):
	status = myBlogs.objects.get(id=int(pk)).active

	if status == True:
		myBlogs.objects.all().filter(id=int(pk)).update(active=False)
	else:
		myBlogs.objects.all().filter(id=int(pk)).update(active=True)
	return HttpResponseRedirect('/blogs/adm/1/')

@login_required
def delete_active(request,pk):
	myBlogs.objects.get(id=pk).delete()
	return HttpResponseRedirect('/blogs/adm/1/')