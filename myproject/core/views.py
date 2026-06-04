from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# home page
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
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