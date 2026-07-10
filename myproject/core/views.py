from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Category
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
# home page
def home(request):
    posts = Post.objects.filter(
        is_published=True
    ).order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
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

def category_post(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(
        category = category,
        is_published = True
    ).order_by('-created_at')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'core/category_posts.html', context)

def contact(request):
    
    # post request
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(f"Name: {name}, Email: {email}, Message: {message}")
            messages.success(request, f"Thanks {name}! Your message was sent.")
            return redirect('contact')
    
    # this is for get request and it will show empty form
    else :
        form = ContactForm()
        
    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)
        