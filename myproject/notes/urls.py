from django.urls import path

from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('<int:note_id>', views.note_detail, name='note_detail'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<int:note_id>/', views.edit_note, name="edit_note"),
]
