
from django.urls import path, re_path

from blogs.views import homepage, admin_page

urlpatterns = [
    path('', homepage, name="homepage"),
    path('adm/',admin_page,name="admin_page")
]
