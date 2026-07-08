from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
# home page
def home(request):
    posts = Post.objects.filter(
        is_published=True
    ).order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'core/home.html', context)

# about page
def about(request):
    context = {
        'Company_Name': 'Amazone',
        'Industry': 'Technology',
    }
    return render(request, 'core/about.html', context)

# contact page
def contact(request):
    return render(request, 'core/contact.html')

# user profile page
def user_profile(request, username):
    return HttpResponse(f"This is about page of {username}")

# user id page
def user_id(request, user_id):
    return HttpResponse(f"Your user id is {user_id}")

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'core/post_detail.html', context)