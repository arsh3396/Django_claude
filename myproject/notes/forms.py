from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError(
                "Title must be at least 5 character"
            )
            
        if title.lower() == 'test':
            raise forms.ValidationError(
                "Please use a meaningful title"
            )
        return title
    
    def clean_content(self):
        content = self.clean_data['content']
        
        if len(content) < 10:
            raise forms.ValidationError(
                "Content must be at least 10 characters"
            )
            
        return content