from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# home page
def home(request):
    context = {
        'name': "Harsh",
        'age': 20,
        'language': 'python',
        'is_logged_in': False,
        'skills': ['Python', 'Java', 'C'],
    }
    return render(request, 'core/home.html', context)

# about page
def about(request):
    return render(request, 'core/about.html')

# contact page
def contact(request):
    return render(request, 'core/contact.html')

# user profile page
def user_profile(request, username):
    return HttpResponse(f"This is about page of {username}")

# user id page
def user_id(request, user_id):
    return HttpResponse(f"Your user id is {user_id}")