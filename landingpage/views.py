from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
	return render(request,'page1.html')

def cabinet(request):
	return render(request,'cabinet.html')

def nantes(request):
	return render(request,'nantes.html')

def contact(request):
	return render(request,'contact.html')

def cadres(request):
	return render(request,'cadres.html')