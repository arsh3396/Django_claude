from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.contrib import messages

# Create your views here.
def notes_list(request):
    notes = Note.objects.all().order_by('-created_at')
    context = {
        "notes": notes 
    }
    return render(request, 'notes/notes_list.html', context)

def note_detail(request, note_id):
    note = get_object_or_404(Note, id = note_id)
    context = {
        "note": note
    }
    return render(request, 'notes/note_detail.html', context)
    
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Note added successfully!")
            return redirect('notes_list')
        
    else: 
        form = NoteForm()
        
    context = {
        'form': form
    }
    
    return render(request, 'notes/add_note.html', context)

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, intstance=note)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated!")
            return redirect('note_detail', note_id=note.id)
    
    else :
        form = NoteForm(instance=note)
        
    context = {
        'form': form,
        'note': note
    }        
    return render(request, 'notes/edit_note.html', context)