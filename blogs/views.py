from django.shortcuts import render, HttpResponse
from blogs.forms import formBlogs
from blogs.models import myBlogs
from django.core.paginator import Paginator

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
	if request.method == "POST":
		forms = formBlogs(request.POST, request.FILES)
		if forms.is_valid():
			forms.save()
		else:
			print(forms)
	forms = formBlogs()
	return render(request,'blogs/input_admin.html',{'forms':forms})