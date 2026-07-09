from django.shortcuts import render, get_object_or_404
from .models import Note

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
    