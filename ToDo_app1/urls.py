from django.urls import path

from ToDo_app1 import views

urlpatterns = [
    path("", views.f_index, name="index"),
    path("adm_index", views.f_admindex, name="adm_index"),
    path("create", views.create, name="create"),
    path("view",views.view, name="view"),
    path("deltask/<int:id>/",views.delete, name="deltask"),
    path("updttask/<int:id>/",views.update_task,name="updttask")
]
