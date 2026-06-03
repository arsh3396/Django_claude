from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# home page
def home(request):
    context = {
        'name': "Harsh",
        'age': 20,
        'language': 'python',
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

# this 
def contact(request):
    return render(request, 'core/contact.html')

def user_profile(request, username):
    return HttpResponse(f"This is about page of {username}")

def user_id(request, user_id):
    return HttpResponse(f"Your user id is {user_id}")