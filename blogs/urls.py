
from django.urls import path, re_path

from blogs.views import homepage, admin_page,logoutme, admin_list, update_active, delete_active

urlpatterns = [
    path('', homepage, name="homepage"),
    path('adm/',admin_page,name="admin_page"),
    path('adm/<str:page>/',admin_list,name="admin_list"),
    path('logout/',logoutme,name="logoutme"),
    path('update/<int:pk>/',update_active,name="update_active"),
    path('delete/<int:pk>/',delete_active,name="delete_active")
]
