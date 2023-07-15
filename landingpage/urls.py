
from django.urls import path

from landingpage.views import cabinet,nantes,contact, cadres, mentions, rgpd,plansite

urlpatterns = [
    path('',cabinet,name='cabinet'),
    path('recrutement-btp-paris-nantes/',nantes,name="nantes"),
    path('contact/',contact,name="contact"),
    path('recrutement-cadres-btp/',cadres,name="cadres"),
    path('mentions/',mentions,name="mentions"),
    path('rgpd/',rgpd,name="rgpd"),
    path('plan-site/',plansite,name="plansite")
]
