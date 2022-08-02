from django.urls import path
from django.http import HttpResponse
from recipes.views import home, contato, sobre

def my_view(request):
    return HttpResponse("It's working")

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]