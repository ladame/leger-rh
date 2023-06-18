from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from blogs.forms import formBlogs
from blogs.models import myBlogs
from django.core.paginator import Paginator

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.contrib import messages

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

	tampilkan_new=True

	return render(request,'blogs/dashboard.html',{'tampilkan_new':tampilkan_new,'olddata':lihatlah,'newdata':newdata})

def detail_article(request,pk):
	try:
		nomor_id = int(pk)
	except:
		nomor_id = 0

	mydata = myBlogs.objects.all().filter(active=True,id=pk).order_by("-id")

	filtered_data = myBlogs.objects.get(id=nomor_id)

	tampilkan_new=False
	return render(request,'blogs/detail_article.html',{'tampilkan_new':tampilkan_new,'olddata':mydata,'newdata':filtered_data})

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
			messages.success(request,"Connexion réussie ! Bienvenue %s"%username)
		else:
			messages.success(request,"Échec de la connexion! S’il vous plaît répéter encore!")
		return HttpResponseRedirect('/blogs/adm/')
		
	else:
		if request.method == "POST":
			forms = formBlogs(request.POST, request.FILES)
			if forms.is_valid():
				forms.save()
				messages.success(request,"Nouvelles ajoutées avec succès!")
			else:
				messages.success(request,"Les nouvelles n’ont pas été ajoutées! La nouvelle a-t-elle déjà été publiée?")
		forms = formBlogs()
		return render(request,'blogs/input_admin.html',{'forms':forms})

def logoutme(request):
	logout(request)
	messages.success(request,"Vous vous êtes déconnecté avec succès !")
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
				usernya = User.objects.get(username=username)
				usernya.set_password(pass1)
				usernya.save()
				messages.success(request,"Mise à jour du mot de passe réussie!")
			else:
				messages.success(request,"Ancien mot de passe erroné! Mise à jour du mot de passe annulée...")
		else:
			messages.success(request,"Les premier et deuxième mots de passe sont différents! Mise à jour du mot de passe annulée...")
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
	messages.success(request,"Nouvelles %s désactivées avec succès (archivées)!"%myBlogs.objects.get(id=int(pk)).title)
	return HttpResponseRedirect('/blogs/adm/1/')

@login_required
def delete_active(request,pk):
	myBlogs.objects.get(id=pk).delete()
	messages.success(request,"La nouvelle a été supprimée avec succès!")
	return HttpResponseRedirect('/blogs/adm/1/')