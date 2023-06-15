
from django.urls import path

from landingpage.views import homepage,cabinet,nantes,contact, cadres

urlpatterns = [
    path('', homepage, name="homepage"),
    path('cabinet-conseil-recrutement-btp/',cabinet,name='cabinet'),
    path('recrutement-btp-paris-nantes/',nantes,name="nantes"),
    path('contact/',contact,name="contact"),
    path('recrutement-cadres-btp/',cadres,name="cadres")
]
