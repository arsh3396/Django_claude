from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name="about"),
    path("user/<str:username>/", views.user_profile, name='userProfile'),
    path("user/<int:user_id>/", views.user_id, name="userId"),
    path("post/<int:post_id>/", views.post_detail, name='post_detail'),
    path("category/<int:category_id>/", views.category_post, name='category_posts'),
]