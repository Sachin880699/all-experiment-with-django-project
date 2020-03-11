from django.urls import path
from.import views

urlpatterns = [
    path("",views.home,name="home"),
    path("other",views.other,name="other"),
    path("form",views.form,name ='form'),
    path("math",views.math,name = 'math')
]