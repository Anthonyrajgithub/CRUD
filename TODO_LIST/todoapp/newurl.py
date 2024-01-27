from django.urls import path
from todoapp import views
urlpatterns = [
    path("",views.display),
    # path("q",views.edit),
    path("add",views.add),
    # path("s",views.remove),
    path('edit/<tid>',views.edit),
    path('delete/<tid>',views.delete),
]